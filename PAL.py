# PAL.py — All-in-one PAL compiler with libraries and error system

# ---------------- Amino acids ----------------
AA_TO_CODON = {
    "MET":"AUG","ALA":"GCU","GLY":"GGU","LYS":"AAA","CYS":"UGU",
    "THR":"ACU","SER":"UCU","TYR":"UAU","PHE":"UUU","LEU":"UUA",
    "VAL":"GUU","GLU":"GAA","ASP":"GAU","ARG":"CGU","ASN":"AAU",
    "GLN":"CAA","PRO":"CCU","HIS":"CAU","ILE":"AUU","TRP":"UGG",
    "STOP":"UAA"
}
CODON_TO_AA = {v:k for k,v in AA_TO_CODON.items()}

import os

# ---------------- Error system ----------------
ERRORS=[]
def log(msg, level="note", line=None):
    ln = f" line {line}" if line else ""
    ERRORS.append(f"[{level}]{ln} {msg}")

# ---------------- Instruction motifs ----------------
INSTRUCTION_TO_MOTIF = {
    "START":["MET"], "END":["STOP"],
    "BIND DNA":["ARG","ARG","GLY","GLU"],
    "BIND RNA":["ARG","SER","GLY","ASN"],
    "BIND PROTEIN":["LEU","ILE","VAL","GLY"],
    "SENSE LIGHT":["TRP","SER","ASP"],
    "SIGNAL NUCLEUS":["ARG","LYS","LYS","ARG"],
    "MOTOR WALK":["LYS","GLU","GLY","ALA"],
    "ATC GFP":["GLY","GLY","GLY","MET","GLY","GLY","THR"]
}

# ---------------- Function parser ----------------
def parse_functions(lines):
    funcs, cur, body = {}, None, []
    for idx, l in enumerate(lines,1):
        lstrip = l.strip()
        if lstrip.upper().startswith("FUNC "):
            cur, body = lstrip[5:].strip().upper(), []
        elif lstrip.upper()=="END FUNC":
            if cur: funcs[cur]=body
            cur=None
        elif cur: body.append(lstrip)
    return funcs

# ---------------- Library import ----------------
# Libraries are Python files in lib/*.py with a variable PAL_LIB
def import_library(lib_name, functions, line_num):
    # First try to import a Python library module (lib/<name>.py with PAL_LIB)
    try:
        lib_module = __import__(f"lib.{lib_name}", fromlist=["PAL_LIB"])
        pal_code = getattr(lib_module, "PAL_LIB")
        funcs_in_lib = parse_functions(pal_code.strip().splitlines())
        functions.update(funcs_in_lib)
        log(f"Imported library module 'lib.{lib_name}'", "note", line=line_num)
        return
    except Exception:
        # fall through to try loading a .pal file from the lib/ directory
        pass

    # Fallback: try to read a .pal file under lib/<lib_name>.pal
    pal_path = os.path.join(os.path.dirname(__file__), "lib", f"{lib_name}.pal")
    try:
        with open(pal_path, "r", encoding="utf-8") as fh:
            pal_code = fh.read()
        funcs_in_lib = parse_functions(pal_code.strip().splitlines())
        functions.update(funcs_in_lib)
        log(f"Imported library file '{lib_name}.pal'", "note", line=line_num)
    except FileNotFoundError:
        log(f"Library not found: 'lib/{lib_name}.py' or '{pal_path}'", "danger", line=line_num)
    except Exception as e:
        log(f"Failed to import library '{lib_name}' (fallback): {e}", "danger", line=line_num)

# ---------------- Compiler ----------------
def mRNA_Compile(pal_code):
    ERRORS.clear()
    lines = pal_code.strip().splitlines()
    functions={}
    main_code=[]
    in_func=False
    cur_func=""
    func_body=[]
    
    for idx,l in enumerate(lines,1):
        lu = l.strip().upper()
        if lu.startswith("FUNC "):
            in_func=True
            cur_func=l[5:].strip().upper()
            func_body=[]
        elif lu=="END FUNC":
            in_func=False
            if cur_func: functions[cur_func]=func_body
        elif in_func:
            func_body.append(l.strip())
        else:
            main_code.append((l.strip(), idx))

    mrna_seq=[]

    def compile_line(line, line_num):
        lu=line.upper()
        if lu.startswith("IMPORT "):
            lib_name=line.split()[1].strip()
            import_library(lib_name, functions, line_num)
        elif lu.startswith("CALL "):
            fn=line[5:].strip()
            if fn not in functions:
                log(f"Unknown function '{fn}'", "warning", line=line_num)
                return
            for fline in functions[fn]:
                compile_line(fline, line_num)
        elif lu in INSTRUCTION_TO_MOTIF:
            motif=INSTRUCTION_TO_MOTIF[lu]
            for aa in motif:
                codon=AA_TO_CODON.get(aa)
                if codon:
                    mrna_seq.append(codon)
                else:
                    log(f"Unknown amino acid '{aa}' in motif '{lu}'","danger", line=line_num)
            if len(motif)>4: log(f"Motif '{lu}' may be slow to compile","note", line=line_num)
        elif lu.startswith("AA "):
            aa=line.split()[1].upper()
            codon=AA_TO_CODON.get(aa)
            if codon: mrna_seq.append(codon)
            else: log(f"Unknown amino acid '{aa}'","warning", line=line_num)
        elif lu.startswith("SEQ "):
            for aa in line.split()[1:]:
                codon=AA_TO_CODON.get(aa.upper())
                if codon: mrna_seq.append(codon)
                else: log(f"Unknown amino acid '{aa}'","warning", line=line_num)
        elif lu!="":
            log(f"Unknown instruction '{line}'","danger", line=line_num)

    for line, idx in main_code:
        if line: compile_line(line, idx)

    return "".join(mrna_seq)

# ---------------- Eukaryotic wrap ----------------
def wrap_mrna_for_eukaryotes(mrna: str) -> str:
    cap = "m7G"
    tail = "AAA(x98)"
    return f"{cap}-{mrna}-{tail}"

# ---------------- Utilities ----------------
def translate_aa_to_rna(motif):
    try: return "".join(AA_TO_CODON[aa] for aa in motif)
    except KeyError as e: log(f"Unknown amino acid {e}", "danger"); return ""

def translate_rna_to_aa(rna):
    return [CODON_TO_AA.get(rna[i:i+3], "?") for i in range(0,len(rna),3)]

def pretty_codons(rna):
    return " ".join(rna[i:i+3] for i in range(0,len(rna),3))
