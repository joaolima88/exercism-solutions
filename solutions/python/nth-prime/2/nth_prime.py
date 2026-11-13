import math

def check_prime(x):
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def primes_generator():
    yield 2
    i = 3
    while True:
        if check_prime(i):
            yield i
        i += 2

def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')

    primes_gen = primes_generator()
    for _ in range(number - 1):
        next(primes_gen)

    return next(primes_gen)