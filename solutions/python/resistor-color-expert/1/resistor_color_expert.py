def resistor_label(colors):

    tolerance= {
    'black':'',
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


    if len (colors) < 4:
        number = ''
        for i in colors:
            number += str(resistance[i])
    elif len(colors) == 4:
        number = ''
        for i in colors[:2]:
            number += str(resistance[i])
        number += resistance[colors[2]] * '0'
    else:
        number = ''
        for i in colors[:3]:
            number += str(resistance[i])
        number += resistance[colors[3]] * '0'

    p_10 = int(number) / int('1' + '0' * (len(str(number))-1))
    number = int(number)

    if len(str(number)) <= 3 and colors[-1] != 'black':
        return f'{str(number)} ohms ±{tolerance[colors[-1]]}'
    elif len(str(number)) <= 3 and colors[-1] == 'black':
        return f'{str(number)} ohms'
    else:
        number = int(number)

        if number < 100000:
                return f'{str(number/1000)} kiloohms ±{tolerance[colors[-1]]}' if str(number/1000)[-1] != '0' else f'{str(round(number/1000))} kiloohms ±{tolerance[colors[-1]]}'
        elif number < 100000000:
                return f'{str(number/1000000)} megaohms ±{tolerance[colors[-1]]}' if str(number/1000000)[-1] != '0' else f'{str(round(number/1000000))} kiloohms ±{tolerance[colors[-1]]}'
        elif number >= 1000000000:
                return f'{str(number/1000000000)} gigaohms ±{tolerance[colors[-1]]}' if str(number/1000000000)[-1] != '0' else f'{str(round(number/1000000000))} kiloohms ±{tolerance[colors[-1]]}'
