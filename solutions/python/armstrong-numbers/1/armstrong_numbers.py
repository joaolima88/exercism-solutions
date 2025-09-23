def is_armstrong_number(number):
    
    lista = []
    y = str(number)
    for i in y:
      lista.append(int(i)**len(y))
    
    if sum(lista) == number:
      return True
    return False 
