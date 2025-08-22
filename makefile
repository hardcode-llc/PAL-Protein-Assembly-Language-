# Makefile for PAL Protein System

# Python interpreter
PYTHON=python3

# Source files
PAL_SRC=PAL.py
PAL_CODE=main.py
LIB_DIR=lib

# Output mRNA file
MRNA_OUT=output_mrna.txt

# Default target
all: compile run

# Compile PAL code to mRNA
compile:
	@echo "[note] Compiling PAL code..."
	$(PYTHON) -c "from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes; \
with open('$(PAL_CODE)') as f: code=f.read(); \
mrna=mRNA_Compile(code); \
mrna_wrapped=wrap_mrna_for_eukaryotes(mrna); \
with open('$(MRNA_OUT)','w') as out: out.write(mrna_wrapped); \
print('[note] Compilation finished, mRNA saved to $(MRNA_OUT)')"

# Run the compiled mRNA
run:
	@echo "[note] Running compiled mRNA sequence..."
	@cat $(MRNA_OUT)
	@echo "\n[note] Execution complete."

# Clean generated files
clean:
	@echo "[note] Cleaning generated files..."
	@rm -f $(MRNA_OUT)
	@echo "[note] Clean complete."

# Phony targets
.PHONY: all compile run clean
