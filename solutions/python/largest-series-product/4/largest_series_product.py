import math

def largest_product(series, size):

    if size > len(series): # span of numbers is longer than number series
        raise ValueError("span must not exceed string length")

    if size < 0: # span of number is negative
        raise ValueError("span must not be negative")


    current_product = 0
    for i in range(len(series)-(size-1)):
        number = series[i:i+size]

        try:
            digits = [int(i) for i in number]
        except ValueError as error:
            raise ValueError("digits input must only contain digits") from error
        if math.prod(digits) > current_product:
            current_product = math.prod(digits)
        else:
            continue
    return current_product