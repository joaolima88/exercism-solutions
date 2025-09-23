def annotate(minefield):
    """
    Function to add the mine counts to empty squares in a completed Minesweeper board.
    The board itself is a rectangle composed of squares that are either empty (' ') or a mine ('*').
    For each empty square, counts the number of mines adjacent to it (horizontally, vertically, diagonally).
    If the empty square has no adjacent mines, leaves it empty. Otherwise replaces it with the adjacent mines count.

    param: list, example: ["  *  ", "  *  ", "*****", "  *  ", "  *  "]
    return: list, example: [" 2*2 ", "25*52", "*****", "25*52", " 2*2 "]
    """

    if not minefield:
        return []

    for idx, i in enumerate(minefield):

        if len(i) != len(minefield[0]):
            raise ValueError("The board is invalid with current input.")

        minefield[idx] = list(i.replace(' ', '0'))

        for letter in i:
            if letter != " " and letter != "*":
                raise ValueError("The board is invalid with current input.")

    for line in minefield:
        for idx, i in enumerate(line):
            if i == '0':
                line[idx] = int(0)


    max_h = len(minefield[0])
    max_v = len(minefield)

    for idx, line in enumerate(minefield):
        for idx2, i in enumerate(line):


            # Check vertical

            # Check vertical down
            if idx+1 < max_v:
                if minefield[idx+1][idx2] == '*' and i != '*':
                    minefield[idx][idx2] += 1

            # Check vertical up
            if idx-1 >= 0:
                if minefield[idx-1][idx2] == '*' and i != '*':
                    minefield[idx][idx2] += 1


            # Check horizontal

            # Check horizontal right
            if idx2+1 < max_h and i != '*':
                if line[idx2+1] == '*':
                    line[idx2] += 1

            # Check horizontal right
            if idx2 > 0 and i != '*':
                if line[idx2-1] == '*':
                    line[idx2] += 1


            # Check diagonal

            # Check diagonal right up
            if idx+1 < max_v and idx2+1 < max_h:
                if minefield[idx+1][idx2+1] == '*' and i != '*':
                    minefield[idx][idx2] += 1

            # Check diagonal left up
            if idx+1 < max_v and idx2-1 >= 0:
                if minefield[idx+1][idx2-1] == '*' and i != '*':
                    minefield[idx][idx2] += 1

            # Check diagonal left down
            if idx-1 >= 0 and idx2+1 < max_h:
                if minefield[idx-1][idx2+1] == '*' and i != '*':
                    minefield[idx][idx2] += 1

            # Check diagonal left down
            if idx-1 >= 0 and idx2-1 >= 0:
                if minefield[idx-1][idx2-1] == '*' and i != '*':
                    minefield[idx][idx2] += 1

    return [''.join(str(i) for i in line).replace('0', ' ') for line in minefield]


