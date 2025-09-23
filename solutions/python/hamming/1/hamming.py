def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
        
    counter=0
    for idx,i in enumerate(strand_a):
        if i != strand_b[idx]:
            counter += 1

    return counter
        
