def is_int(num):
    if num.is_integer():
        return int(num)
    else:
        return num

def resistor_label(colors):

    tolerance= {
    'grey':'0.05%',
    'violet':'0.1%',
    'blue':'0.25%',
    'green':'0.5%',
    'brown':'1%',
    'red':'2%',
    'gold':'5%',
    'silver':'10%'
    }

    resistance={
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

    number = ''
    if len (colors) < 4:
        for i in colors:
            number += str(resistance[i])
    elif len(colors) == 4:
        for i in colors[:2]:
            number += str(resistance[i])
        number += resistance[colors[2]] * '0'
    else:
        for i in colors[:3]:
            number += str(resistance[i])
        number += resistance[colors[3]] * '0'

    number = int(number)
    if number < 1000 and colors[-1] in tolerance:
        return f'{str(number)} ohms ±{tolerance[colors[-1]]}'
    elif number < 1000 and colors[-1] not in tolerance:
        return f'{str(number)} ohms'
    elif number < 100000:
        return f'{str(is_int(number/1000))} kiloohms ±{tolerance[colors[-1]]}'
    elif number < 100000000:
        return f'{str(is_int(number/1000000))} megaohms ±{tolerance[colors[-1]]}'
    elif number >= 1000000000:
        return f'{str(is_int(number/1000000000))} gigaohms ±{tolerance[colors[-1]]}'