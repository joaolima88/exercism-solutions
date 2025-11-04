def transpose(text):

    x = text.split('\n')
    m = max(map(len, x))

    for i in range(len(x)):
        spaces = '*' * (m - len(x[i]))
        x[i] = x[i] + spaces

    ind = 0
    tran = []

    while ind != m:
        line=''
        for i in x:
            line += i[ind]
        tran.append(line)
        ind += 1

    t=[]
    for i in tran:
        t.append(i.rstrip('*'))

    tran = '\n'.join(t).replace('*', ' ')
 
    return tran