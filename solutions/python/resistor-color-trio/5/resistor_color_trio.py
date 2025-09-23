def label(colors):

    d={
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
    }

    number = int(str(d[colors[0]]) + str(d[colors[1]]) + str(d[colors[2]] * '0'))

    if len(str(number)) <= 3:
        return str(number) + ' ohms'
    else:
        z = min(filter(lambda i: i != 0 , [number//1000, number//1000000, number//1000000000]))
   
        if z == number//1000:
            return str(z) + ' kiloohms'
        if z == number//1000000:
            return str(z) + ' megaohms'
        if z == number//1000000000:
            return str(z) + ' gigaohms'