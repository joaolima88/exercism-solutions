def convert(input_grid):

    if len(input_grid) %4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(map(lambda x: x%3 != 0 , list(map(len,input_grid)))):
        raise ValueError("Number of input columns is not a multiple of three")



    d = {" || _ _  || ": '0',
        "         || ": '1',
        "  | ___  |  ": '2',
        "    ___  || ": '3',
        " |   _   || ": '4',
        " |  ___   | ": '5',
        " || ___   | ": '6',
        "    _    || ": '7',
        " || ___  || ": '8',
        " |  ___  || ": '9'}



    ind1, ind2, counter = 0, 4, 0
    final, number = '', ''

    while ind2 < len(input_grid)+1:
        for i in zip(*input_grid[ind1:ind2]):
            number += ''.join(i)
            counter += 1
            if counter == 3:
                if number in d:
                    final += d[number]
                    number = ''
                    counter = 0
                else:
                    final += '?'
                    number = ''
                    counter = 0

        final += ','
        ind1 += 4
        ind2 += 4


    return final[:-1]

