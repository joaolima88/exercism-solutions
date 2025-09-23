def commands(binary_str):
    
    l = ['Reverse the order of the operations in the secret handshake', 'jump', 'close your eyes', 'double blink', 'wink']
    res = []
    
    
    l = l[5-len(binary_str):]

    for i in range(0,len(binary_str)):
        if binary_str[i] == '1':
            res.append(l[i])


    if res and res[0] == 'Reverse the order of the operations in the secret handshake':
        return res[1:]
    else:
        return res[::-1]