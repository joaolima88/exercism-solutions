def classify(number):
  if number>0: 
    count=0
    for i in range(1, number):
      if number % i == 0:
        count+=i
    if count == number:
      return 'perfect'
    elif count > number:
      return 'abundant'
    elif count < number:
      return 'deficient'
  else:
    raise ValueError("Classification is only possible for positive integers.")