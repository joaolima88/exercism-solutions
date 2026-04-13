# Score categories.
# Change the values as you see fit.

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice, category):
        match category:
            case 1:
                return dice.count(1)
            case 2:
                return dice.count(2) * 2
            case 3:
                return dice.count(3) * 3
            case 3:
                return dice.count(3) * 2
            case 4:
                return dice.count(4) * 4
            case 5:
                return dice.count(5) * 5
            case 6:
                return dice.count(6) * 6
            case 7:
                x = list(set(dice))
                if len(x) == 2:
                    if sorted([dice.count(x[0]), dice.count(x[-1])]) == [2,3]:
                        return sum(dice)
                    else:
                        return False
                else:
                    return False
            case 8:
                x = list(set(dice))
                if len(x)>1:
                    y=max((dice.count(x[0]),x[0]),(dice.count(x[1]),x[1]))
                    if y[0] == 4:
                        return y[-1]*4
                    else:
                        return False
                else:
                    return 4*x[0]
            case 9:
                return 30 if sorted(dice) == [1,2,3,4,5] else 0
            case 10:
                return 30 if sorted(dice) == [2,3,4,5,6] else 0     
            case 11:
                return sum(dice)
            case 12:
                return 50 if len(set(dice)) == 1 else 0