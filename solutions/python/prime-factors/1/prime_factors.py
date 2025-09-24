def check_prime(x):
    import math
    for i in range(2,round(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def next_prime(number):
        if check_prime(number+1):
            return number+1
        else:
            return next_prime(number+1)

def factors(value):
    primes = []
    current_prime = 2

    while value != 1:
        if value % current_prime == 0:
            primes.append(current_prime)
            value = value / current_prime
        else:
            current_prime = next_prime(current_prime)
    
    return primes