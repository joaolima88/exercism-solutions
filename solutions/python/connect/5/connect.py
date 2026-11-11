class ConnectGame:
    def __init__(self, board):
        self.board = board

    def make_board(self, board_str):
        return [i.lstrip().replace(' ', '') for i in board_str.splitlines()]

    def get_Xs(self, board):

        S, E = [], []

        for idx, i in enumerate(board):
            if i[0] == 'X':
                S.append((idx, 0))
            if i[-1] == 'X':
                E.append((idx, len(i)-1))

        return S, E

    def next_pieces(self, piece):
        piece_right = (piece[0], piece[-1]+1)
        piece_left = (piece[0], piece[-1]-1)
        piece_up = (piece[0]-1, piece[-1])
        piece_up_right = (piece[0]-1, piece[-1]+1)
        piece_down = (piece[0]+1, piece[-1])
        piece_down_left = (piece[0]+1, piece[-1]-1)

        return [piece_up, piece_up_right, piece_right, piece_left, piece_down, piece_down_left]

    def valid_X_pieces(self, p, board, end_Xs, visited_pos):
        next_p = self.next_pieces(p)
        v_p = []
        size = len(board[0])

        for i in next_p:
            row = i[0]
            col = i[1]
            if row >= 0 and row < len(board) and col >= 0 and col <= size:
                next_piece = (row, col)
                if board[row][col] == 'X' and next_piece not in visited_pos:
                    v_p.append(next_piece)
        return v_p

    def search_X(self, board, piece, end_Xs, visited_pos):
        if visited_pos is None:
            visited_pos = []
        if piece in end_Xs:
            updated_visited = visited_pos + [piece]
            return (updated_visited,)
        else:
            updated_visited = visited_pos + [piece]
            valid_p = self.valid_X_pieces(piece, board, end_Xs, updated_visited)
            if valid_p:
                return valid_p, updated_visited
        return None

    def recursive_search_X(self, board, piece, end_Xs, visited_pos):
        new_pieces = self.search_X(board, piece, end_Xs, visited_pos)
        if new_pieces:
            if len(new_pieces) == 1:
                return new_pieces
            else:
                next_ps = new_pieces[0]
                new_visited_pos = new_pieces[1]
                for i in next_ps:
                    res = self.recursive_search_X(board, i, end_Xs, new_visited_pos)
                    if res:
                        return res
                return None

    def get_winner_X(self):
        b = self.make_board(self.board)
        S_X, E_X = self.get_Xs(b)
        for i in range(len(S_X)):
            start_piece = S_X[i]
            result = self.recursive_search_X(b, start_piece, E_X, visited_pos=[])
            if result:
                return True
        return False

    def get_Os(self, board):
        return [(0, idx) for idx, i in enumerate(board[0]) if i == 'O'], [(len(board)-1, idx) for idx, i in enumerate(board[-1]) if i == 'O']
        
    def valid_O_pieces(self, p, board, end_Xs, visited_pos):
        next_p = self.next_pieces(p)
        v_p = []
        size = len(board)-1
        for i in next_p:
            row = i[0]
            col = i[1]
            if row >= 0 and row < len(board) and col >= 0 and col <= size:
                next_piece = (row, col)
                if board[row][col] == 'O' and next_piece not in visited_pos:
                    v_p.append(next_piece)
        return v_p

    def search_O(self, board, piece, end_Os, visited_pos):
        if visited_pos is None:
            visited_pos = []
        if piece in end_Os:
            updated_visited = visited_pos + [piece]
            return (updated_visited,)
        else:
            updated_visited = visited_pos + [piece]
            valid_p = self.valid_O_pieces(piece, board, end_Os, updated_visited)
            if valid_p:
                return valid_p, updated_visited
        return None

    def recursive_search_O(self, board, piece, end_Os, visited_pos):
        new_pieces = self.search_O(board, piece, end_Os, visited_pos)
        if new_pieces:
            if len(new_pieces) == 1:
                return new_pieces
            else:
                next_ps = new_pieces[0]
                new_visited_pos = new_pieces[1]
                for i in next_ps:
                    res = self.recursive_search_O(board, i, end_Os, new_visited_pos)
                    if res:
                        return res
                return None

    def get_winner_O(self):
        b = self.make_board(self.board)
        S_O, E_O = self.get_Os(b)
        for i in range(len(S_O)):
            start_piece = S_O[i]
            result = self.recursive_search_O(b, start_piece, E_O, visited_pos=[])
            if result:
                return True
        return False

    def get_winner(self):
        if self.get_winner_O():
            return 'O'
        if self.get_winner_X():
            return 'X'
        return ''