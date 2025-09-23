d={
  'black': [0,'ohms'],
  'brown': [1,'ohms'] ,
  'red': [2,'ohms'],
  'orange': [3,'kiloohms'],
  'yellow': [4,'kiloohms'],
  'green': [5,'kiloohms'],
  'blue': [6,'megaohms'],
 'violet': [7,'megaohms'],
  'grey': [8,'megaohms'],
  'white': [9,'gigaohms']
}


def label(colors):

  result1=''
  for i in colors[:2]:
    result1 += str(d[i][0])

  x=str(int(result1)* 10**d[colors[2]][0])

  z=[chave for chave in d if d[chave][0]==x.count('0')]

  y=d[z[0]][1]
  
  if x.count('0') > 3:
    x=10**(x.count('0')%3) * int(x.replace('0',''))
  elif x.count('0') == 3:
    x=x.strip('0')
      
  return str(int(x)) + ' ' + d[z[0]][1]


