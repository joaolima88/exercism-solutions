def steps(n, lista=None):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    if lista is None:
        lista = [n]  # Initialize the list with the starting number

    if n != 1:
        if n % 2 == 0:
            lista.append(n//2)
            steps(n//2, lista)
        else:
            lista.append(n*3 + 1)
            steps(n * 3 + 1, lista)
    return len(lista)-1