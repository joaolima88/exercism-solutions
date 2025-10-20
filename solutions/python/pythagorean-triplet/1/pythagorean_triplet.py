def triplets_with_sum(number):
    import math
    ul = round(number/(2 + math.sqrt(2)))
    r=[]

    for i in range(1, ul):
        a = i
        b = (number**2 - (2*number*a)) / (2*(number-a))
        if b == int(b) and b > a:
            c = number - i - b
            if c > b:
                r.append([round(a),round(b),round(c)])

    return r