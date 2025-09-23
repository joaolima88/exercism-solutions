d1={
  'black': 0,
  'brown':1,
  'red': 2,
  'orange': 3,
  'yellow': 4,
  'green': 5,
  'blue': 6,
  'violet': 7,
  'grey': 8,
  'white': 9,
}

d2={
  'black': 'ohms',
  'brown': 'ohms' ,
  'red': 'kiloohms',
  'orange': 'kiloohms',
  'yellow': 'kiloohms',
  'green': 'kiloohms',
  'blue': 'megaohms',
 'violet': 'megaohms',
  'grey': 'megaohms',
  'white': 'gigaohms'
}


d3={
  0: 'ohms',
  1: 'ohms' ,
  2: 'ohms',
  3: 'kiloohms',
  4: 'kiloohms',
  5: 'kiloohms',
  6: 'megoohms',
  7: 'megoohms',
  8: 'megoohms',
  9: 'gigagoohms'
}



def label(colors):
  result1=''
  result2=None
  for i in colors[:2]:
    result1 += str(d1[i])

  result2 = str(10**d1[colors[2]])
  x=result1 + result2[1:]

  y=d3[x.count('0')]
  if x.count('0') > 3:
    x=10**(x.count('0')%3) * int(x.replace('0',''))
  elif x.count('0') == 3:
    x=x.replace('0', '')
  return str(int(x)) + ' ' + d2[colors[2]]