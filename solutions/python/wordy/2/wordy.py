def answer(question):

    

    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    lista_2 = ['plus', 'minus', 'multiplied', 'divided']
    question = question[:-1]

    formula=[]
    for i in question.split():
        if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
            formula.append(int(i))
        elif i in lista_2:
            formula.append(i)


    if len(formula) == 0:
        raise ValueError("syntax error")

    while len(formula) > 1:
        try:
            x_value = formula[0]
            y_value = formula[2]
            symbol = formula[1]
            remainder = formula[3:]

            if symbol == "plus":
                formula = [x_value + y_value] + remainder
            elif symbol == "minus":
                formula = [x_value - y_value] + remainder
            elif symbol == "multiplied":
                formula = [x_value * y_value] + remainder
            elif symbol == "divided":
                formula = [x_value / y_value] + remainder
            else:
                raise ValueError("syntax error")
        except:
            raise ValueError("syntax error")

    return formula[0]
