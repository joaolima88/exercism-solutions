def rows(letter):

  resultado = []
  Lista_alfa=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  lista_letras=[]

  for i in Lista_alfa:
    if i != letter:
      lista_letras.append(i)
    else:
      break
  lista_letras.insert(len(lista_letras),letter)

  lista_letras_rev = lista_letras[::-1][1:]

  l1,l2,l3,l4 = 1, (len(lista_letras)) - 2, (len(lista_letras_rev)*2) - 3, 1

  for i in lista_letras:
    if i != 'A':
      resultado.append((l2*' ') + i + (l1*' ') + i + (l2*' '))
      l1 += 2
      l2 -= 1
    else:
      resultado.append(((len(lista_letras)-1) * ' ') + i + ((len(lista_letras)-1)*' '))

  for i in lista_letras_rev:
    if i != 'A':
      resultado.append((l4*' ') + i + (l3*' ') + i + (l4*' '))
      l3 -= 2
      l4 += 1
    else:
      resultado.append(((len(lista_letras_rev))*' ') + i + ((len(lista_letras_rev))*' '))
  return resultado
