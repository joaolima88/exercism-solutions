def is_armstrong_number(number):
    
    lista = []
    y = str(number)
    for i in y:
      lista.append(int(i)**len(y))
    
    return True if sum(lista) == number else False
    
