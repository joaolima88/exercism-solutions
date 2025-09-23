def square_root(number, a=1):
    return a if a*a == number else square_root(number, a+1)
        
    
