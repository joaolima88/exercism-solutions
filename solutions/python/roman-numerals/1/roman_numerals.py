def find_closest_numbers(n, res=None):
    if res is None:
        res = []
    
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    new_numbers = [i for i in numbers if len(str(i)) == len(str(n))]

    if n in new_numbers:
        res.append(n)
        return res
    else:
        diff = n
        cn = 0
        for i in new_numbers:
            if n - i < diff and n - i > 0:
                diff = n - i
                cn = i

    res.append(cn)
    return find_closest_numbers(diff, res)

def roman(number):

    y = str(number)
    z = len(y)-1
    l=[]

    for i in y:

        if i == '0':
            z -= 1
            continue
        else:
            l.append(int(i + str('0' * z)))
            z -= 1

    normal = {
                 1:"I",
                 5:"V",
                 10:"X",
                 50:"L",
                 100:"C",
                 500:"D",
                 1000:"M"
            }

    special = {
                 4:"IV",
                 9:"IX",
                 40:"XL",
                 90:"XC",
                 400:"CD",
                 900:"CM"
            }

    new_l = []
    for i in l:
        if i in special:
            new_l.append(i)
        elif i in normal:
            new_l.append(i)
        else:
            num = find_closest_numbers(i)
            new_l = new_l + num

    final_number=[]

    for i in new_l:
        if i in special:
            final_number.append(special[i])
        elif i in normal:
            final_number.append(normal[i])

    return ''.join(final_number)

