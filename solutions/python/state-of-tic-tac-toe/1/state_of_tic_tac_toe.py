def check_win(wining_position, positions):
    return all(item in positions for item in wining_position)

def gamestate(board):

    X = []
    O = []
    space = None

    ind = 0
    for line in board:
        for pos, mark in enumerate(line):
            if mark == 'X': 
                X.append(pos+1+ind)
            if mark == 'O':
                O.append(pos+1+ind)
            elif mark == ' ':
                space = 1
        ind += 3

    if len(O) > len(X):
        raise ValueError("Wrong turn order: O started")
    if len(X) - len(O) > 1:
        raise ValueError("Wrong turn order: X went twice")

    wining_pos = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    X_w = []
    O_w = []

    for i in wining_pos:
        X_w.append(check_win(i, X))
        O_w.append(check_win(i, O))

    if any(X_w) and any(O_w):
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif any(X_w):
        return 'win'
    elif any(O_w):
        return 'win'
    elif space:
        return 'ongoing'
    else:
        return 'draw'
