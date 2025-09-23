def value(colors):
    
    rc = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    lista =[]
    for c in colors[0:2]:
        lista.append(rc.index(c))
        
    conv_1 = str(lista)
    digitos = ''.join([n for n in conv_1 if n.isdigit()])
    return int(digitos)