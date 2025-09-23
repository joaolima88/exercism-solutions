def square(number):
    if number <= 64 and number >= 1:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")  


def total():
    
  squares = []  
  for n in range (1,65):
          
    squares.append(square(n)) 
    
  return sum(squares)  