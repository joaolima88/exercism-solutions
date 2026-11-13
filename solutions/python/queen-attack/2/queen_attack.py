class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.pos = []

        if self.row < 0:
            raise ValueError("row not positive")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.row > 7:
            raise ValueError("row not on board")
        if self.column > 7:
            raise ValueError("column not on board")

    
    def can_attack(self, another_queen):
            opp_row = another_queen.row
            opp_column = another_queen.column
    
            if opp_row == self.row and opp_column == self.column:
                raise ValueError("Invalid queen position: both queens in the same square")
    
            if opp_row == self.row or opp_column == self.column:
                return True
    
            if abs(self.row - opp_row) == abs(self.column - opp_column):
                return True
    
            return False 

