def make_board(game):
    board = []
    space = '*'

    for i in game.splitlines():
        board.append(space + i.lstrip().replace(' ', '')+ space)
        space += '*'
    return board

def get_starter_Xs(board):

    pieces = []

    for idx1, i in enumerate(board):
        if 'X' in i:
            spaces = i.count('*')//2
            idx2 = spaces
            if i[idx2] == 'X':
                piece=(idx1, idx2)
                pieces.append(piece)
    return pieces

def get_end_Xs(board):

    pieces = []

    for idx1, i in enumerate(board):
        if 'X' in i:
            spaces = i.count('*')//2
            idx2 = (len(i) - 1) - spaces
            if i[idx2] == 'X':
                piece = (idx1, idx2)
                pieces.append(piece)
    return pieces

def next_X_pieces(piece):
    piece_up = (piece[0]-1, piece[-1])
    piece_up_left = (piece[0]-1, piece[-1]-1)
    piece_right = (piece[0], piece[-1]+1)
    piece_left = (piece[0], piece[-1]-1)
    piece_down = (piece[0]+1, piece[-1])
    piece_down_right = (piece[0]+1, piece[-1]+1)

    return [piece_up, piece_up_left, piece_right, piece_left, piece_down, piece_down_right]

def valid_X_pieces(p, board, end_Xs, visited_pos):
    next_p = next_X_pieces(p)
    v_p = []

    for i in next_p:
        row = i[0]
        col = i[1]
        if row >= 0 and row < len(board):
            size = len(board[row]) - 1
            if col >= 0 and col <= size:
                next_piece = (row, col)
                if board[row][col] == 'X' and next_piece not in visited_pos:
                    v_p.append(next_piece)

    return v_p


def search_X(board, piece, end_Xs, visited_pos):

    if visited_pos is None:
        visited_pos = []

    if piece in end_Xs:
        updated_visited = visited_pos + [piece]
        return (updated_visited,)
    else:
        updated_visited = visited_pos + [piece]
        valid_p = valid_X_pieces(piece, board, end_Xs, updated_visited)
        if valid_p:
            return valid_p, updated_visited

    return None


def recursive_search_X(board, piece, end_Xs, visited_pos):

    new_pieces = search_X(board, piece, end_Xs, visited_pos)

    if new_pieces:
        if len(new_pieces) == 1:
            return new_pieces
        else:
            next_ps = new_pieces[0]
            new_visited_pos = new_pieces[1]

            for i in next_ps:
                res = recursive_search_X(board, i, end_Xs, new_visited_pos)
                if res:
                    return res
            return None

def get_winner_X(board):
    b = make_board(board)
    S_X = get_starter_Xs(b)
    E_X = get_end_Xs(b)

    for i in range(len(S_X)):
        start_piece = S_X[i]
        result = recursive_search_X(b, start_piece, E_X, visited_pos=[])
        if result:
            return True
    return False


def get_starter_Os(board):

    pieces = []

    for idx1, i in enumerate(board[0]):
        if 'O' in i:
            piece=(0, idx1)
            pieces.append(piece)
    return pieces

def get_end_Os(board):

    pieces = []

    for idx1, i in enumerate(board[-1]):
        if 'O' in i:
            piece=(len(board)-1, idx1)
            pieces.append(piece)
    return pieces

def next_O_pieces(piece):
    piece_up = (piece[0]-1, piece[-1])
    piece_up_left = (piece[0]-1, piece[-1]-1)
    piece_right = (piece[0], piece[-1]+1)
    piece_left = (piece[0], piece[-1]-1)
    piece_down = (piece[0]+1, piece[-1])
    piece_down_right = (piece[0]+1, piece[-1]+1)

    return [piece_up, piece_up_left, piece_right, piece_left, piece_down, piece_down_right]

def valid_O_pieces(p, board, end_Xs, visited_pos):
    next_p = next_O_pieces(p)
    v_p = []

    for i in next_p:
        row = i[0]
        col = i[1]
        if row >= 0 and row < len(board):
            size = len(board[row]) - 1
            if col >= 0 and col <= size:
                next_piece = (row, col)
                if board[row][col] == 'O' and next_piece not in visited_pos:
                    v_p.append(next_piece)

    return v_p


def search_O(board, piece, end_Os, visited_pos):

    if visited_pos is None:
        visited_pos = []

    if piece in end_Os:
        updated_visited = visited_pos + [piece]
        return (updated_visited,)
    else:
        updated_visited = visited_pos + [piece]
        valid_p = valid_O_pieces(piece, board, end_Os, updated_visited)
        if valid_p:
            return valid_p, updated_visited

    return None


def recursive_search_O(board, piece, end_Os, visited_pos):

    new_pieces = search_O(board, piece, end_Os, visited_pos)

    if new_pieces:
        if len(new_pieces) == 1:
            return new_pieces
        else:
            next_ps = new_pieces[0]
            new_visited_pos = new_pieces[1]

            for i in next_ps:
                res = recursive_search_O(board, i, end_Os, new_visited_pos)
                if res:
                    return res
            return None

def get_winner_O(board):
    b = make_board(board)
    S_O = get_starter_Os(b)
    E_O = get_end_Os(b)

    for i in range(len(S_O)):
        start_piece = S_O[i]
        result = recursive_search_O(b, start_piece, E_O, visited_pos=[])
        if result:
            return True
    return False

def get_final_winner(game):
    if get_winner_O(game):
        return 'O'
    if get_winner_X(game):
        return 'X'
    else:
        return ''

class ConnectGame:
    def __init__(self, board):
        self.board = board
    
    def get_winner(self):
        return get_final_winner(self.board)

