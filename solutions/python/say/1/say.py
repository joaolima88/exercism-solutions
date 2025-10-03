def clean(d):
    if d:
        if len(d) == 3:
            if d[0] == '0':

                if d[1] == '0':

                    if d[2] == '0':
                        return ''
                    else:
                        return d[2]

                else:
                    return d[1:]

            else:
                return d

        elif len(d) == 2:
            if d[0] == '0':
                if d[1] == '0':
                    return ''
                else:
                    return d[1]
            else:
                return d
        else:
            if d == '0':
                return ''
            else:
                return d
    else:
        return d



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
        r_num = str(num)[::-1]
        n1, n2, n3, n4, n5 = "", "", "", "", ""
        counter = 0

        while counter < len(r_num):
            if len(n1) < 2:
                n1 += r_num[counter]
                counter += 1
            elif len(n2) < 1:
                n2 += r_num[counter]
                counter += 1
            elif len(n3) < 3:
                n3 += r_num[counter]
                counter += 1
            elif len(n4) < 3:
                n4 += r_num[counter]
                counter += 1
            else:
                n5 += r_num[counter]
                counter += 1
        
        
        n5,n4,n3,n2,n1 = num_to_word(clean(n5[::-1])), num_to_word(clean(n4[::-1])), num_to_word(clean(n3[::-1])), num_to_word(clean(n2[::-1])), num_to_word(clean(n1[::-1]))
        n5,n4,n3,n2,n1 = n5 +' billion ' if n5 else ' ', n4 +' million ' if n4 else ' ', n3 + ' thousand ' if n3 else ' ', n2 + ' hundred ' if n2 else ' ', n1 if n1 else ' '     
        return ' '.join([n5.strip(), n4.strip(), n3.strip(), n2.strip(), n1.strip()]).replace('  ', ' ').strip()

       