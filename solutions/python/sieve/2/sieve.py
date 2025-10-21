def primes(limit):
    if limit < 2:
        return []
    p=[]
    for i in range(2,limit+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            p.append(i)

    return p