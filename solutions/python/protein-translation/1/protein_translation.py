def proteins(strand):
    prot=[]
    aa = {
            "Methionine": ["AUG"],
            "Phenylalanine": ["UUU", "UUC"],
            "Leucine": ["UUA", "UUG"],
            "Serine": ["UCU", "UCC", "UCA", "UCG"],
            "Tyrosine": ["UAU", "UAC"],
            "Cysteine": ["UGU", "UGC"],
            "Tryptophan": ["UGG"],
            "STOP": ["UAA", "UAG", "UGA"]
        }


    for i in range(0,len(strand),3):
        codon = strand[i:i+3]
        for a,c in aa.items():
            if codon in c and a == "STOP":
                return prot
            elif codon in c:
                prot.append(a)
    return prot
        
        