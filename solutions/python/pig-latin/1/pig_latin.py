import re

def R1(t):
    return t + 'ay'

def R2(t):
  result=''
  lista_2=['a','e','i','o','u']
  for i in t:
    if i in lista_2:
      return t[t.index(i):]+t[:t.index(i)] + 'ay'

def R3(t):
  x = re.search("qu", t)
  return t[list(x.span())[-1]:] + t[:list(x.span())[-1]] + 'ay'

def R4(t):
  for i in t:
    if i in 'y':
      return t[t.index(i):]+t[:t.index(i)] + 'ay'


def translate(text):

  lista_3 = []

  for word in text.split():
    if not word.startswith(('a','e','i','o','u')) and not word.startswith(("xr","yt")):

      if re.search("qu", word):
        lista_3.append(R3(word))

      elif re.search("y", word) and word[0] != 'y':
        if 'y' in word:
          a = word[:word.index('y')]
        if re.findall("[aeiou]", a):
          lista_3.append(R2(word))
        else:
          lista_3.append(R4(word))

      else:
        lista_3.append(R2(word))

    else:
     lista_3.append(R1(word))

  return ' '.join(lista_3)