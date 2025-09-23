def encode(plain_text):
  lista=[]
  chars = "abcdefghijklmnopqrstuvwxyz"
  result = ''.join([i for i in plain_text if i.isalnum()])
  trans = str.maketrans(chars + chars.upper() , chars[::-1] + chars[::-1].upper())
  x = result.translate(trans)
  y = x.lower()
  for i in range(-(-len(y)//5)):
    lista.append(y[0:5])
    y = y[5:]
  return ' '.join(lista)


def decode(ciphered_text):
  lista=[]
  chars = "abcdefghijklmnopqrstuvwxyz"
  result = ''.join([i for i in ciphered_text if i.isalnum()])
  trans = str.maketrans(chars[::-1] + chars[::-1].upper(), chars + chars.upper())
  return result.translate(trans)
