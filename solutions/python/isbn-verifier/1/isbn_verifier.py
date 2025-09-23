def is_valid(isbn):
  lista = []
  result = ''.join(char for char in isbn if char.isalnum())
  index = 10

  if len(result) != 10 or not result[0:-1].isdigit() or result == '' or (result[-1] != 'X' and result[-1].isnumeric() == False):
    return False
  else:
    for c in result[0:-1]:
      lista.append(int(c) * index)
      index -= 1

  if result[-1] == 'X':
    lista.append(10)
  else:
    lista.append(int(result[-1]))
  return sum(lista) % 11 == 0
