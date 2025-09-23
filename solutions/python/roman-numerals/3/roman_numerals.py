def roman(number: int) -> str:

    numbers = [1000,   900, 500, 400,  100,  90,  50,  40,  10,  9,   5,  4,    1]
    names   = [  'M', 'CM', 'D', 'CD', 'C',  'XC','L', 'XL', 'X','IX','V','IV', 'I']
    res = ""
    
    while (number > 0):
        for i, val in enumerate(numbers):
            if (number >= val):
                res += names[i]
                number = number - val
                break
    return res