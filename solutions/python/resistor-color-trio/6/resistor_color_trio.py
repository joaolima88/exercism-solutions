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
        p_10 = min(filter(lambda i: i != 0 , [number//1000, number//1000000, number//1000000000]))

        if p_10 == number//1000:
            return str(p_10) + ' kiloohms'
        if p_10 == number//1000000:
            return str(p_10) + ' megaohms'
        if p_10 == number//1000000000:
            return str(p_10) + ' gigaohms'