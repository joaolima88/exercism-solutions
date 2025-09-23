import re

def ope(num_1,num_2,word):
  if word == 'plus':
    return num_1 + num_2
  elif word == 'minus':
    return num_1 - num_2
  elif word == 'multiplied':
    return num_1 * num_2
  elif word == 'divided':
    return num_1 / num_2

def eval(question):

  lista_1 = ['What', 'is', 'by', 'plus', 'minus', 'multiplied', 'divided']
  lista_2 = ['plus', 'minus', 'multiplied', 'divided']
  question = question[:-1]
  numbers = [int(word) for word in question.split() if word.isdigit() or (word.startswith('-') and word[1:].isdigit())]
  operadores = [word for word in question.split() if word in lista_2]
  
  dd=[]
  for i in question.split():
    if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
      dd.append(int(i))
    elif i in lista_2:
      dd.append(i)

  if len(numbers) == 0 or len(operadores)==0:
    for i in question.split():
      if i not in lista_1 and not i.isdigit() and not (i.startswith('-') and i[1:].isdigit()):
        raise ValueError("unknown operation")
  if len(numbers) != len(operadores) + 1 or len(operadores)==0:
    if len(numbers) == 1 and len(operadores) == 0:
      return numbers[0]
    elif len(numbers) == 0:
      raise ValueError("syntax error")
    elif len(numbers) != len(operadores)+1:
      raise ValueError("syntax error")
  if len(numbers) != 0 and len(operadores) != 0:
    for i in dd:
      if i in lista_2:
        try:
          if type(dd[dd.index(i)+1]) != type(dd[dd.index(i)-1]) or dd.index(i) == 0:
            raise ValueError("syntax error")
        except IndexError:
          raise ValueError("syntax error")

def answer(question):

  if eval(question):
    return eval(question)
  else:
    lista_1 = ['What', 'is', 'by', 'plus', 'minus', 'multiplied', 'divided']
    lista_2 = ['plus', 'minus', 'multiplied', 'divided']
    question = question[:-1]
    numbers = [int(word) for word in question.split() if word.isdigit() or (word.startswith('-') and word[1:].isdigit())]
    operadores = [word for word in question.split() if word in lista_2]
    lista_3 = []
    ind1, ind2 = 1,2

    lista_3.append(ope(numbers[0],numbers[1],operadores[0]))
    for i in range(len(operadores)-1):
      lista_3.append(ope(lista_3[-1],numbers[ind2],operadores[ind1]))
      ind1 += 1
      ind2 += 1

  return lista_3[-1]

