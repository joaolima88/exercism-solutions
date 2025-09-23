def check_prime(x):
    import math
    for i in range(2,round(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def prime(number):

    if number <= 0:
        raise ValueError('there is no zeroth prime')

    i = 2
    counter = 0

    while counter < number:
        if check_prime(i):
            counter += 1
            i += 1
        else:
            i += 1

    return i-1