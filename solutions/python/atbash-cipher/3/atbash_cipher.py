def encode(plain_text):
  lista=[]
  chars = "abcdefghijklmnopqrstuvwxyz"
  result = ''.join([i for i in plain_text if i.isalnum()])
  trans = str.maketrans(chars + chars.upper() , chars[::-1] + chars[::-1].upper())
  x = result.lower().translate(trans)
  for i in range(-(-len(x)//5)):
    lista.append(x[0:5])
    x = x[5:]
  return ' '.join(lista)


def decode(ciphered_text):
  chars = "abcdefghijklmnopqrstuvwxyz"
  result = ''.join([i for i in ciphered_text if i.isalnum()])
  trans = str.maketrans(chars[::-1] + chars[::-1].upper(), chars + chars.upper())
  return result.translate(trans)
