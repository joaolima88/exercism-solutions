def line_up(name, number):
    number = str(number)
    d={'1': 'st', '2': 'nd', '3': 'rd'}
    if number[-1] in d and number[-2:] not in ['11', '12', '13']:
        suffix = d[number[-1]]
    else:
        suffix = 'th'

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"