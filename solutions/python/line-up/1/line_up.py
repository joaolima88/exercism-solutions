def line_up(name, number):

    n = str(number)
    suffix = None

    if len(n) == 1:
        last_n = n[-1]

        if last_n == '1':
            suffix = 'st'
        elif last_n == '2':
            suffix = 'nd'
        elif last_n == '3':
            suffix = 'rd'
        else:
            suffix = 'th'
    else:
        last_n = n[-2:]

        if last_n == '11' or last_n == '12' or last_n == '13':
            suffix = 'th'
        else:
            if last_n[-1] == '1':
                suffix = 'st'
            elif last_n[-1] == '2':
                suffix = 'nd'
            elif last_n[-1] == '3':
                suffix = 'rd'
            else:
                suffix = 'th'


    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'