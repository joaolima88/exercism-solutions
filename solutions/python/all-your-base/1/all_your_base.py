def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    for i in digits:
        if i < 0 or i >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    number = sum([i * input_base**(len(digits)-idx-1) for idx,i in enumerate(digits)])

    if number // output_base == 0:
        re = []
        re.append(number % output_base)
        return re
    else:
        re = []
        while number // output_base != 0:
            re.append(number % output_base)
            number = number // output_base
            if number // output_base == 0:
                re.append(number % output_base)
                return re[::-1]