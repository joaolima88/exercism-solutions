def decode(string):
    string = string.replace(' ','*')
    l = []
    ini = 0

    for idx,i in enumerate(string):
        if i.isalpha() or i == '*':
            l.append(string[ini:idx+1])
            ini = idx+1

    for idx,i in enumerate(l):
        if len(i)>1:
            l[idx] = i[-1] * int(i[:-1])

    return ''.join(l).replace('*', ' ')


def encode(string):
    if not string:
        return ''

    current_letter = string[0]
    counter = 0
    final = ''

    for i in string:
        if i == current_letter:
            counter += 1
        elif i != current_letter:
            if counter != 1:
                final += str(counter) + current_letter
                current_letter = i
                counter = 1
            else:
                final += current_letter
                current_letter = i
                counter = 1

    if counter != 1:
        final += str(counter) + current_letter
    else:
        final += current_letter
    return final
