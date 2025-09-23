def to_rna(dna_strand):
    conv = {
        "A":"U", 
        "T":"A",
        "G":"C",
        "C":"G"
    }

    return "".join(conv[base] for base in dna_strand)
