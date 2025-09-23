def classify(number):
  if number>0: 
    lista=[]
    count=1
    while count < number:
      if number % count == 0:
        lista.append(count)
      count+=1
    if sum(lista) == number:
      return 'perfect'
    elif sum(lista) > number:
      return 'abundant'
    elif sum(lista) < number:
      return 'deficient'
  else:
    raise ValueError("Classification is only possible for positive integers.")