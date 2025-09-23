def saddle_points(matrix):

    if not all(len(sublista) == len(matrix[0]) for sublista in matrix):
            raise ValueError('irregular matrix')

    cord=[]
    for idx1, i in enumerate(matrix):
        for idx2, j in enumerate(i):
            if j == max(i):
                cord.append((j,idx1,idx2))

    final = cord.copy()
    for i in cord:
        column = i[2]
        for j in range(len(matrix)):
            if matrix[j][column] < i[0]:
                final.remove(i)
                break

    return [{'row': i[1]+1, 'column': i[2]+1} for i in final]