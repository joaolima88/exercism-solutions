import math

def get_span_products(series, size):
    
    for i in range(len(series) - size + 1):
        n = series[i:i+size]
        try:
            yield math.prod(int(d) for d in n)
        except ValueError as error:
            raise ValueError("digits input must only contain digits") from error

def largest_product(series, size):

    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")

    return max(get_span_products(series, size), default=1)