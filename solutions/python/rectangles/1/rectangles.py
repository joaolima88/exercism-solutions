def combinations(positions):
    vertices = []

    for i in positions:
        for j in positions:
            if j == i or tuple(sorted((i,j))) in vertices:
                continue
            else:
                vertices.append(tuple(sorted((i,j))))

    return vertices

def generate_cords(strings):

    d = {}

    for i in range(len(strings)):
        line = strings[i]
        if '+' in line:
            for j in range(len(line)):
                if line[j] == '+':
                    if i in d:
                        d[i].append(j)
                    else:
                        d[i] = [j]

    for i in d.keys():
        d[i] = combinations(d[i])

    return d

def valid_lines(strings):
    pos = generate_cords(strings)

    d = {}

    for i in pos.items():
        lines = i[1]
        for j in lines:
            p1 = j[0]
            p2 = j[1]
            if ' ' not in strings[i[0]][p1:p2+1]:
                if i[0] in d:
                    d[i[0]].append(j)
                else:
                    d[i[0]] = [j]


    return(d)


def rectangles(strings):

    p = valid_lines(strings)
    d = {}

    for i in p.items():
        row = i[0]
        vertices = i[1]
        for v in vertices:
            v1 = v[0]
            v2 = v[1]
            if (v1,v2) not in d:
                d[(v1,v2)] = [((v1,v2), row)]
            else:
                d[(v1,v2)].append(((v1,v2), row))


    rectangle_counter = 0

    for i in d.values():
        for cord in i:
            current_cord = cord
            for j in i:
                if j == current_cord:
                    continue
                else:
                    p1 = current_cord[0][0]
                    p2 = current_cord[0][1]
                    start = current_cord[1] + 1
                    stop = j[1]

                    idx = 0

                    while start+idx < stop:
                        side_1 = strings[start+idx][p1]
                        side_2 = strings[start+idx][p2]

                        if side_1 not in ['|', '+'] or side_2 not in ['|', '+']:
                            break
                        else:
                            idx += 1
                    if start+idx == stop:
                        rectangle_counter += 1



    return rectangle_counter
