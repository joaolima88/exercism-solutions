def steps(n):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    c = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            c += 1
        else:
            n = n*3 + 1
            c += 1
        
    return c