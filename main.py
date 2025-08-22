from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes

pal_code = """
IMPORT binding
IMPORT signaling
IMPORT motor
IMPORT transport
IMPORT modification
IMPORT regulation
IMPORT fluorescent

START
# Sense environment
CALL SIGNAL_LIGHT_TEMP
CALL SIGNAL_PRESSURE_MAGNETIC

# Conditional behavior based on environment
IF LIGHT_HIGH
    CALL MOTOR_WALK
    CALL SIGNAL_NUCLEUS
ELSE
    CALL MOTOR_SLIDE
    CALL SIGNAL_MEMBRANE
END IF

IF TEMP_HIGH
    CALL MODIFY_PHOS
    CALL REGULATE_COMPLEX
ELSE
    CALL MODIFY_ACETYL
END IF

# Adaptive binding
IF DNA_PRESENT
    CALL BIND_DNA_COMPLEX
ELSE
    CALL BIND_PROTEIN_COMPLEX
END IF

# Monitoring and visualization
CALL FLUORESCENT_TAG_COMPLEX

END
"""

mrna = mRNA_Compile(pal_code)
injectable = wrap_mrna_for_eukaryotes(mrna)
print("Universal CRISPR Protein v1", injectable)
