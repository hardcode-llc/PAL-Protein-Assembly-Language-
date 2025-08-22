# ⚠️ WARNING: DEMO ONLY. Due to sub-liceinsing this demo Cannot injected this into humans or animals.
# If you do you will face leagle restrictions and a fine
from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes

# ---------- 1. Basic Universal Vaccine ----------
basic_vaccine_demo = """
IMPORT binding
IMPORT signaling
IMPORT regulation
IMPORT modification
IMPORT fluorescent

START
# Detect multiple pathogens
CALL SENSE_PATHOGEN
IF PATHOGEN_DETECTED
    CALL BIND_ANTIGEN
    CALL SIGNAL_NUCLEUS
    CALL MODIFY_ADAPTIVE_RESPONSE
    CALL FLUORESCENT_TAG_COMPLEX
    NOTE "Immune activation sequence engaged"
ELSE
    CALL MONITOR_ENVIRONMENT
END IF
END
"""

# ---------- 2. Protein that Cleans Up Oil Spills ----------
oil_cleanup_demo = """
IMPORT binding
IMPORT motor
IMPORT transport
IMPORT modification

START
# Detect oil molecules
CALL SENSE_HYDROCARBON
IF OIL_DETECTED
    CALL BIND_OIL
    CALL MOTOR_SWARM
    CALL TRANSPORT_TO_SURFACE
    CALL MODIFY_DEGRADATION
    NOTE "Oil breakdown sequence engaged"
ELSE
    CALL MONITOR_WATER
END IF
END
"""

# ---------- 3. Self-Healing Material Protein ----------
self_healing_demo = """
IMPORT signaling
IMPORT binding
IMPORT modification
IMPORT motor

START
# Detect structural damage
CALL SENSE_DAMAGE
IF DAMAGE_DETECTED
    CALL BIND_MATERIAL_FIBERS
    CALL SIGNAL_REPAIR
    CALL MOTOR_CONTRACT
    CALL MODIFY_CROSSLINK
    NOTE "Self-healing routine activated"
ELSE
    CALL MONITOR_STRUCTURE
END IF
END
"""

# ---------- 4. CO2 Cleanup Protein ----------
co2_cleanup_demo = """
IMPORT binding
IMPORT transport
IMPORT modification
IMPORT regulation

START
# Detect CO2 concentration
CALL SENSE_CO2
IF CO2_HIGH
    CALL BIND_CO2
    CALL TRANSPORT_CAPTURE
    CALL MODIFY_CHEMICAL_CONVERSION
    CALL REGULATE_METABOLISM
    NOTE "CO2 capture routine active"
ELSE
    CALL MONITOR_AIR
END IF
END
"""

# ---------- 5. Nasal Spray Protein for Multiple Respiratory Diseases ----------
nasal_spray_demo = """
IMPORT binding
IMPORT signaling
IMPORT transport
IMPORT modification
IMPORT fluorescent

START
# Detect respiratory pathogens
CALL SENSE_RESP_PATHOGEN
IF PATHOGEN_PRESENT
    CALL BIND_PATHOGEN
    CALL SIGNAL_NUCLEUS
    CALL MODIFY_IMMUNE_RESPONSE
    CALL TRANSPORT_CLEARANCE
    CALL FLUORESCENT_TAG_COMPLEX
    NOTE "Nasal spray defense sequence active"
ELSE
    CALL MONITOR_NASAL_PASSAGES
END IF
END
"""

# ---------- Run All Demos ----------
demos = [
    ("Basic Universal Vaccine", basic_vaccine_demo),
    ("Oil Cleanup Protein", oil_cleanup_demo),
    ("Self-Healing Material Protein", self_healing_demo),
    ("CO2 Cleanup Protein", co2_cleanup_demo),
    ("Nasal Spray Respiratory Protein", nasal_spray_demo),
]

for name, pal_code in demos:
    print("\n" + "="*60)
    print(f"{name} (DEMO ONLY)")
    print("-"*60)
    mrna = mRNA_Compile(pal_code)
    wrapped = wrap_mrna_for_eukaryotes(mrna)
    print("m7G-...-AAA(x98) [simulation]")
    print(wrapped[:120] + " ...")  # show first 120 chars
