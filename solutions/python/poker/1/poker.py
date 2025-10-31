def suits(hand):
    card_suits = [i for i in hand if i in "HCSD"]
    card_suits_count = len(set(card_suits))

    if card_suits_count == 1:
        return True
    else:
        return False

def rank(hand):
    import re
    d = {"K":"13", "Q":"12", "J":"11"}
    ranks = ' '.join([d[i[0]] if i[0] in d.keys() else i for i in hand.split(' ')])
    ranks = re.findall(r'\d+', ranks)
    ranks = [int(i) if i.isdigit() else int(d[i]) for i in ranks]

    if 'A' in hand and sum(ranks)==14:
        ranks.append(1)
        return sorted(ranks)
    elif 'A' in hand:
        A_count = hand.count('A')
        ranks.extend([14]*A_count)
        return sorted(ranks)
    return sorted(ranks)

def is_sequential(hand):
    _rank = rank(hand)

    for i in range(len(_rank)-1):
        if _rank[i+1] - _rank[i] != 1:
            return False
    else:
        return True

def hand_classifier(hands):
    r=[]
    for hand in hands:
        if suits(hand)  and sum(rank(hand)) == 60 and is_sequential(hand):
            r.append((10,))

        elif suits(hand)  and is_sequential(hand):
            r.append((9, max(rank(hand))))

        elif max([rank(hand).count(i) for i in set(rank(hand))]) == 4:
            cards = rank(hand)
            main_group = sum([i for i in cards if cards.count(i) == 4])
            kicker = sum([i for i in cards if cards.count(i) != 4])
            r.append((8, main_group, kicker))

        elif len(set(rank(hand))) == 2:
            c1, c2 = set(rank(hand))
            triplet, pair = sorted([(rank(hand).count(c1), c1), (rank(hand).count(c2), c2)], reverse = True)
            r.append((7, triplet[1], pair[1]))

        elif suits(hand) and not is_sequential(hand):
            c1, c2, c3, c4, c5 = sorted(rank(hand), reverse = True)
            r.append((6, c1, c2, c3, c4, c5))

        elif not suits(hand) and is_sequential(hand):
            r.append((5, max(rank(hand))))

        elif len(set(rank(hand))) == 3:
            c1, c2, c3 = set(rank(hand))
            rank_count = [(rank(hand).count(c1), c1), (rank(hand).count(c2), c2), (rank(hand).count(c3), c3)]

            if max(rank_count)[0] == 3:
                triplet_t, kicker1_t, kicker2_t = sorted(rank_count, reverse = True)

                _, triplet = triplet_t
                _, kicker1 = kicker1_t
                _, kicker2 = kicker2_t

                r.append((4, triplet, kicker1, kicker2))

            elif max(rank_count)[0] == 2:
                pair1_t, pair2_t, kicker_t = sorted(rank_count, reverse = True)

                _, pair1 = pair1_t
                _, pair2 = pair2_t
                _, kicker = kicker_t

                r.append((3, pair1, pair2, kicker))

        elif len(set(rank(hand))) == 4:
            c1, c2, c3, c4 = set(rank(hand))
            rank_count = [(rank(hand).count(c1), c1), (rank(hand).count(c2), c2), (rank(hand).count(c3), c3), (rank(hand).count(c4), c4)]

            pair_t, kicker1_t, kicker2_t, kicker3_t = sorted(rank_count, reverse = True)

            _, pair = pair_t
            _, kicker1 = kicker1_t
            _, kicker2 = kicker2_t
            _, kicker3 = kicker3_t

            r.append((2, pair, kicker1, kicker2, kicker3))

        else:
            c1, c2, c3, c4, c5 = sorted(rank(hand), reverse = True)
            r.append((1, c1, c2, c3, c4, c5))

    return r

def best_hands(hands):


    clean_hands = hand_classifier(hands)
    max = sorted(hand_classifier(hands), reverse = True)[0]
    final =[]

    for i in range(len(clean_hands)):
        if clean_hands[i] == max:
            final.append(hands[i])

    return final


