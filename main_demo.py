# ⚠️ WARNING: DEMO ONLY. Due to sub-liceinsing this demo Cannot injected this into humans or animals.
# If you do you will face leagle restrictions and a fine
from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes

# ---------- CANCER PROTEIN ----------
cancer_demo = """
IMPORT binding
IMPORT signaling
IMPORT regulation
IMPORT modification
IMPORT motor
IMPORT fluorescent

START

# Detect abnormal cell growth
CALL SENSE_TUMOR_SIGNAL
IF DNA_DAMAGE_HIGH
    CALL BIND_TUMOR_SUPPRESSOR
    CALL SIGNAL_NUCLEUS
    CALL MODIFY_APOPTOSIS
    CALL MOTOR_WALK
    IF CHECKPOINT_FAIL
        CALL SIGNAL_MEMBRANE
        CALL REGULATE_TRANSCRIPTION
        NOTE "Escalation protocol engaged"
    ELSE
        CALL REGULATE_GROWTH
    END IF
ELSE
    CALL MONITOR_CELLS
END IF

# Visualization
CALL FLUORESCENT_TAG_COMPLEX
END
"""

# ---------- ALZHEIMER'S PROTEIN ----------
alz_demo = """
IMPORT binding
IMPORT signaling
IMPORT transport
IMPORT modification
IMPORT regulation
IMPORT fluorescent

START

# Detect amyloid beta plaques
CALL SENSE_AMYLOID
IF PLAQUE_HIGH
    CALL BIND_AMYLOID
    CALL TRANSPORT_CLEARANCE
    CALL SIGNAL_MICROGLIA
    CALL MODIFY_PHOS
    IF NEURON_SIGNAL_LOW
        CALL SIGNAL_NUCLEUS
        CALL PROTEIN_FOLDING
        NOTE "High plaque escalation routine"
    ELSE
        CALL MONITOR_NEURONS
    END IF
ELSE
    CALL SIGNAL_MEMORY_PATHWAY
END IF

# Visualization
CALL ATC_RFP
END
"""

# ---------- DIABETES PROTEIN ----------
diabetes_demo = """
IMPORT signaling
IMPORT transport
IMPORT regulation
IMPORT modification
IMPORT motor
IMPORT fluorescent

START

# Detect high glucose
CALL SENSE_GLUCOSE_HIGH
IF GLUCOSE_LEVEL_HIGH
    CALL SIGNAL_INSULIN
    CALL TRANSPORT_GLUCOSE
    CALL REGULATE_METABOLISM
    CALL MOTOR_CONTRACT
    IF CELL_RESPONSE_FAIL
        CALL MODIFY_ACETYL
        CALL SIGNAL_NUCLEUS
        NOTE "Metabolic escalation engaged"
    ELSE
        CALL MONITOR_GLUCOSE
    END IF
ELSE
    CALL SIGNAL_NORMAL
END IF

# Visualization
CALL ATC_GFP
END
"""

# ---------- HEART DISEASE PROTEIN ----------
heart_demo = """
IMPORT binding
IMPORT signaling
IMPORT transport
IMPORT regulation
IMPORT motor
IMPORT fluorescent

START

# Detect arterial stress
CALL SENSE_PRESSURE
CALL SENSE_ELECTRICAL
IF PLAQUE_PRESENT
    CALL BIND_LDL
    CALL TRANSPORT_CLEARANCE
    CALL REGULATE_CHOLESTEROL
    CALL SIGNAL_REPAIR
    CALL MOTOR_WALK
    IF CARDIAC_RISK_HIGH
        CALL SIGNAL_NUCLEUS
        CALL MODIFY_SUMO
        NOTE "Critical heart support engaged"
    ELSE
        CALL MONITOR_HEART
    END IF
ELSE
    CALL SIGNAL_CARDIAC_STRENGTH
END IF

# Visualization
CALL ATC_LUCIFERASE
END
"""

# ---------- DRUG RESISTANCE PROTEIN ----------
drugres_demo = """
IMPORT binding
IMPORT signaling
IMPORT modification
IMPORT motor
IMPORT fluorescent

START

# Detect pathogens
CALL SENSE_PATHOGEN
IF PATHOGEN_PRESENT
    CALL SIGNAL_IMMUNE_RESPONSE
    CALL BIND_PATHOGEN
    CALL MODIFY_ADAPTIVE_ATTACK
    CALL MOTOR_SWARM
    IF DRUG_EFFECTIVE_LOW
        CALL SIGNAL_NUCLEUS
        CALL REGULATE_TRANSCRIPTION
        NOTE "Adaptive drug-resistance response triggered"
    ELSE
        CALL MONITOR_PATHOGEN
    END IF
ELSE
    CALL SIGNAL_NORMAL
END IF

# Visualization
CALL ATC_RFP
END
"""

# ---------- Run all demos ----------
demos = [
    ("Cancer Demo", cancer_demo),
    ("Alzheimer's Demo", alz_demo),
    ("Diabetes Demo", diabetes_demo),
    ("Heart Disease Demo", heart_demo),
    ("Drug-Resistance Demo", drugres_demo),
]

for name, pal_code in demos:
    print("\n" + "="*60)
    print(f"{name} (DEMO ONLY)")
    print("-"*60)
    mrna = mRNA_Compile(pal_code)
    wrapped = wrap_mrna_for_eukaryotes(mrna)
    print("m7G-...-AAA(x98) [simulation]")
    print(wrapped[:120] + " ...")  # show first 120 chars
