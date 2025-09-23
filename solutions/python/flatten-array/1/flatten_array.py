def flatten(iterable):
    
    new_iter=str(iterable).replace('[','').replace(']','').replace(' ', '')
    list_new_iter=new_iter.split(',')

    numbers=[]

    for i in list_new_iter:
        if i.isnumeric():
            numbers.append(int(i))
        elif '-' in i:
            numbers.append(int(i))
    return numbers