def fill_matrix(size, matrix, n, line, column, dir, first):

    counter = 0
    for i in matrix:
        if 0 in i:
            counter += 1


    if counter != 0:
        if first == True:
            for idx, i in enumerate(matrix[0]):
                matrix[line][idx] += n + 1
                n = matrix[line][idx]
                column = idx
            return fill_matrix(5, matrix, n, line+1, column, dir = 'right', first = False)

        else:

            if dir == 'up':
                for idx, i in enumerate(matrix[line]):
                    if i == 0:
                        matrix[line][idx] = matrix[line][idx] + n + 1
                        n = matrix[line][idx]
                        column = idx


                return fill_matrix(5, matrix, n, line+1, column, dir = 'right', first = False)

            if dir == 'down':
                u = 0
                for idx, i in enumerate(matrix[line]):
                    if i == 0:
                        if u == 0:
                            column = idx
                            u += 1
                        matrix[line][idx] = matrix[line][idx] + n + matrix[line].count(0)

                n = matrix[line][column]
                return fill_matrix(5, matrix, n, line-1, column, dir = 'left', first = False)

            if dir == 'right':
                for idx in enumerate(matrix):
                    if matrix[idx[0]][column] == 0:
                        matrix[idx[0]][column] += n+1
                        n = matrix[idx[0]][column]
                        line = idx[0]

                return fill_matrix(5, matrix, n, line, column-1, dir = 'down', first = False)


            if dir == 'left':
                u = 0
                n_zeros=0
                for idx in enumerate(matrix):
                    if matrix[idx[0]][column] == 0:
                        n_zeros += 1

                for idx in enumerate(matrix):
                    if matrix[idx[0]][column] == 0:

                        if u == 0:
                            line = idx[0]
                            u += 1

                        matrix[idx[0]][column] += n + n_zeros
                        n_zeros -= 1

                n = matrix[line][column]
                return fill_matrix(5, matrix, n, line, column+1, dir = 'up', first = False)

    else:
        return matrix


        
def spiral_matrix(size):
    matrix = [[0 for i in range(size)]for i in range(size)]
    if size > 1:
        return fill_matrix(size, matrix, n = 0, line = 0, column = 0, dir = None, first = True)
    elif size == 1:
        return [[1]]
    else:
        return []
