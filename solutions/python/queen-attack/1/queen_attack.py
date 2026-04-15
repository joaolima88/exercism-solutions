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

    def attack_positions(self):
        self.x_1 = self.row
        self.x_2 = self.row

        self.y_1 = self.column
        self.y_2 = self.column

        while self.x_1<7 or self.x_2>0 or self.y_1<7 or self.y_2>0:
            self.x_1 += 1
            self.x_2 -= 1

            self.y_1 += 1
            self.y_2 -= 1

            self.pos.append((self.x_1,self.y_1))
            self.pos.append((self.x_2,self.y_1))
            self.pos.append((self.x_1,self.y_2))
            self.pos.append((self.x_2,self.y_2))
        return self.pos
        

    def can_attack(self, another_queen):
        opp_row = another_queen.row
        opp_column = another_queen.column

        if opp_row ==self.row and opp_column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        if opp_row == self.row:
            return True
        if opp_column == self.column:
            return True
    
        return (opp_row,opp_column) in self.attack_positions()

