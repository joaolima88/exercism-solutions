from itertools import product

def check_cell(matrix, cell_cords):

    column  = cell_cords[0]
    row = cell_cords[1]

    if matrix[column][row] == 1:
        return 1
    return 0

def tick(matrix):

    if matrix:

        n = len(matrix)
        cords = [i for i in range(n)]
        cells = list(product(cords, cords))
        new_matrix = [row[:] for row in matrix]

        for cell in cells:
            row = cell[0]
            col = cell[1]
            neighbours = 0

            right = col+1
            left = col-1
            up = row-1
            down = row+1
            dig_1 = (up,right)
            dig_2 = (up,left)
            dig_3 = (down, right)
            dig_4 = (down, left)
            
            directions = [(row,right), (row,left), (up,col), (down,col), dig_1, dig_2, dig_3, dig_4]
            new_directions = [dir for dir in directions if dir in cells]

            for i in new_directions:
                neighbours += check_cell(matrix, i)

            if neighbours < 2 or neighbours > 3:
                new_matrix[row][col] = 0
            elif neighbours == 3:
                new_matrix[row][col] = 1
            elif neighbours == 2 and matrix[row][col] == 1:
                new_matrix[row][col] = 1
            else:
                new_matrix[row][col] = 0

        return new_matrix
    return matrix