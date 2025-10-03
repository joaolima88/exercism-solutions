def clean(d):
    if d:
        if d == '000' or d =='00' or d=='0':
            return ''
        else:
            for idx,i in enumerate(d):
                if i != '0':
                    return d[idx:]
    else:
        return ''


def num_to_word(x):
    numbers = {
        '0':'zero', '1': "one", '2': "two", '3': "three", '4': "four", '5': "five",
        '6': "six", '7': "seven", '8': "eight", '9': "nine", '10': "ten",
        '11': "eleven", '12': "twelve", '13': "thirteen", '14': "fourteen",
        '15': "fifteen", '16': "sixteen", '17': "seventeen", '18': "eighteen",
        '19': "nineteen", '20': "twenty", '30': "thirty", '40':'forty', '50': "fifty",
        '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'
    }

    if x in numbers:
        return numbers[x]
    elif len(x) == 2:
        return numbers[x[0]+'0'] + '-' + numbers[x[1]]
    elif len(x) == 3:
        if x[1:] == '00':
            return numbers[x[0]] + ' hundred'
        else:
            if x[1:] in numbers:
                return numbers[x[0]] + ' hundred ' + numbers[x[1:]]
            else:
                if x[1] != '0':
                    return numbers[x[0]] + ' hundred ' + numbers[x[1]+'0'] + '-' + numbers[x[2]]
                else:
                    return numbers[x[0]] + ' hundred ' + numbers[x[2]]


def say(num):

    if num == 0:
        return 'zero'
    if num < 0:
        raise ValueError("input out of range")
    if num > 999_999_999_999:
        raise ValueError("input out of range")
    else:
        formatted_number = f"{num:,}"
        groups = (['']*(4-len(formatted_number.split(',')))) +formatted_number.split(',')
        n4,n3,n2,n1 = groups
        n4,n3,n2,n1 = num_to_word(clean(n4)), num_to_word(clean(n3)), num_to_word(clean(n2)), num_to_word(clean(n1))
        n4,n3,n2,n1 = n4 +' billion ' if n4 else ' ', n3 + ' million ' if n3 else ' ', n2 + ' thousand ' if n2 else ' ', n1 if n1 else ' '
        return ' '.join([n4.strip(), n3.strip(), n2.strip(), n1.strip()]).replace('  ', ' ').strip()