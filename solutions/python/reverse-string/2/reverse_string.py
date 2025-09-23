def reverse(text):
    
    y=[i for i,l in enumerate(text)]
    y.sort(reverse=True)
    
    z=''
    for i in y:
      z=z+(text[i])
        
    return z