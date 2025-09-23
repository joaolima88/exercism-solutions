def rotate(text, key):

  x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  y=list(range(0,26))
  dic1=dict(zip(x,y))
  dic2=dict(zip(y,x))
  result = ''

  for i in text:
    if i.isupper():
      i = i.lower()
      rotated_index = (dic1[i] + key) % 26
      nresult = dic2[rotated_index]
      result += nresult.upper()
    elif i in dic1:
      rotated_index = (dic1[i] + key) % 26
      result += dic2[rotated_index]
    else:
      result += i

  return result