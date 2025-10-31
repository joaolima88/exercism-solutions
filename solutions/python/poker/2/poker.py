def suits(hand: str) -> bool:
    card_suits = [card[-1] for card in hand.split()]
    return len(set(card_suits)) == 1

def rank(hand: str) -> list:
    V = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10}
    
    ranks = []
    for card in hand.split():
        value = card[:-1] 
        if value in V:
            ranks.append(V[value])
        else:
            ranks.append(int(value))
    
    sorted_ranks = sorted(ranks)
    if 14 in sorted_ranks and sorted_ranks == [2, 3, 4, 5, 14]:
        return [1, 2, 3, 4, 5]
    
    return sorted_ranks

def is_sequential(hand: str) -> bool:
    _rank = rank(hand)
    return all(b - a == 1 for a, b in zip(_rank, _rank[1:]))

def hand_classifier(hands: list) -> list:
    r = []
    for hand in hands:
        ranks = rank(hand)
        is_flush = suits(hand)
        is_straight = is_sequential(hand)
        rank_counts = sorted([(ranks.count(i), i) for i in set(ranks)], reverse=True)
        
        # Royal Flush
        if is_flush and is_straight and sum(ranks) == 14:
            r.append((10,))
        # Straight Flush
        elif is_flush and is_straight:
            r.append((9, max(ranks)))
        # Four of a Kind
        elif rank_counts[0][0] == 4:
            r.append((8, rank_counts[0][1], rank_counts[1][1]))
        # Full House
        elif rank_counts[0][0] == 3 and rank_counts[1][0] == 2:
            r.append((7, rank_counts[0][1], rank_counts[1][1]))
        # Flush
        elif is_flush:
            r.append((6, *sorted(ranks, reverse=True)))
        # Straight
        elif is_straight:
            r.append((5, max(ranks)))
        # Three of a Kind
        elif rank_counts[0][0] == 3:
            r.append((4, rank_counts[0][1], rank_counts[1][1], rank_counts[2][1]))
        # Two Pair
        elif rank_counts[0][0] == 2 and rank_counts[1][0] == 2:
            r.append((3, rank_counts[0][1], rank_counts[1][1], rank_counts[2][1]))
        # One Pair
        elif rank_counts[0][0] == 2:
            r.append((2, rank_counts[0][1], rank_counts[1][1], rank_counts[2][1], rank_counts[3][1]))
        # High Card
        else:
            r.append((1, *sorted(ranks, reverse=True)))
    
    return r

def best_hands(hands: list) -> list:
    classified = hand_classifier(hands)
    best_score = max(classified)
    return [hands[idx] for idx, score in enumerate(classified) if score == best_score]


