def horizontal(tabuleiro):

    for line in tabuleiro:


        max = len(line)
        min = 0

        for idx, i in enumerate(line):
            if idx+1 < max and i != '*':
                if line[idx+1] == '*':
                    line[idx] += 1

            if idx > min and i != '*':
                if line[idx-1] == '*':
                    line[idx] += 1

def vertical(tabuleiro):

    max = len(tabuleiro)
    min = 0

    for idx, line in enumerate(tabuleiro):
        for idx2, i in enumerate(line):

            if idx+1 < max:
                if tabuleiro[idx+1][idx2] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1

            if idx-1 >= min:
                if tabuleiro[idx-1][idx2] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1

def diagonal_baixo(tabuleiro):

    max_v = len(tabuleiro)
    max_h = len(tabuleiro[0])
    min = 0

    for idx, line in enumerate(tabuleiro):
        for idx2, i in enumerate(line):

            if idx+1 < max_v and idx2+1 < max_h:
                if tabuleiro[idx+1][idx2+1] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1

            if idx+1 < max_v and idx2-1 >= min:
                if tabuleiro[idx+1][idx2-1] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1

def diagonal_cima(tabuleiro):

    min_v = 0
    max_h = len(tabuleiro[0])
    min = 0

    for idx, line in enumerate(tabuleiro):
        for idx2, i in enumerate(line):

            if idx-1 >= min_v and idx2+1 < max_h:
                if tabuleiro[idx-1][idx2+1] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1

            if idx-1 >= min_v and idx2-1 >= min:
                if tabuleiro[idx-1][idx2-1] == '*' and i != '*':
                    tabuleiro[idx][idx2] += 1


def annotate(minefield):

    if not minefield:
        return []

    
    
    l=minefield
    alf = [" ", "*"]
    
    com = len(minefield[0])
    for i in minefield:
        if len(i) != com:
            raise ValueError("The board is invalid with current input.")
        for letter in i:
            if letter not in alf:
                raise ValueError("The board is invalid with current input.")

                
    for idx, i in enumerate(l):
        l[idx] = list(i.replace(' ', '0'))

    for line in l:
        for idx, i in enumerate(line):
            if i == '0':
                line[idx] = int(0)


    horizontal(minefield)
    vertical(minefield)
    diagonal_cima(minefield)
    diagonal_baixo(minefield)

    res = []

    for line in minefield:
        x= ''.join(str(i) for i in line)
        res.append(x)

    for idx, i in enumerate(res):
        res[idx]=i.replace('0', ' ')

    return res
    
