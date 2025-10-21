def mult(x, primes):
    for i in primes:
        if x % i == 0:
            return False
       
    return True

def primes(limit):
    if limit < 2:
        return []
        
    numbers = [i for i in range(2,limit+1)]
    p = [2]

    for n in numbers:
        if mult(n,p):
            p.append(n)
        else:
            continue

    return p