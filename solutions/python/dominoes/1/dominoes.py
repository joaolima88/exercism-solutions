def valid_chain(dominoes, chain):
    return (len(dominoes) == len(chain)) and (chain[0][0] == chain[-1][1])


def create_chain(dominoes, idx):
    pieces = [i for i in dominoes]

    first_stone = dominoes[idx]
    side_1 = first_stone[0]
    side_2 = first_stone[1]

    chain = [first_stone]
    pieces.remove(first_stone)


    for _ in range(len(dominoes)):
        for p in pieces:

            if p[0] == side_2:
                pieces.remove(p)
                chain.append(p)
                side_2 = p[1]

            elif p[1] == side_2:
                pieces.remove(p)
                p = p[::-1]
                chain.append(p)
                side_2 = p[1]

    return chain, pieces



def fix_chain(chain, pieces=None):

    if pieces:

        r_pieces = [i[::-1] for i in pieces]

        for i in range(len(chain)-1):
            d1 = chain[i]
            d2 = chain[i+1]

            d1_1 = d1[1]
            d2_0 = d2[0]


            if (d1_1, d2_0) in pieces:
                chain.insert(i+1, (d1_1, d2_0))
                idx = pieces.index((d1_1, d2_0))
                r_pieces.remove(r_pieces[idx])
                pieces.remove((d1_1, d2_0))

            elif (d2_0, d1_1) in r_pieces:
                chain.insert(i+1, (d2_0, d1_1))
                idx = r_pieces.index((d2_0, d1_1))
                pieces.remove(pieces[idx])
                r_pieces.remove((d2_0, d1_1))

        return chain, pieces

    else:
        return chain


def can_chain(dominoes):

    if dominoes:

        c,p = fix_chain(create_chain(dominoes,0))

        if c and not p:
            if len(c) > 1:
                return c
            else:
                if c[0][0] == c[0][1]:
                    return c 


        else:
            size = len(dominoes)
            for i in range(1,size):
                final_chain, final_pieces = fix_chain(create_chain(dominoes, i))
                if not final_pieces:
                    if valid_chain(dominoes, final_chain):
                        return final_chain
                        
    else:
        return []


