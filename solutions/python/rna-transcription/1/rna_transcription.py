def to_rna(dna_strand):
    conv = {
        "A":"U", 
        "T":"A",
        "G":"C",
        "C":"G"
    }

    rna = ""
    for i in dna_strand:
        rna += conv[i]
    return rna
    
