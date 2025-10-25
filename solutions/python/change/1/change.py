def combine_mults(new_coins, available_coins):

    final =[]
    unique_coins = [(i,new_coins.count(i)) for i in set(new_coins)]

    for i in unique_coins:
        temp = [j for j in new_coins if j == i[0]]

        for _ in temp:
            if sum(temp) in available_coins and len(temp) > 1:
                final.append((i[0], temp.count(i[0]), sum(temp)))
                break
            elif len(temp) > 1:
                temp = temp[1:]
            else:
                break

    if not final:
        return new_coins

    for i in final:
        c1 = i[0]
        c2 = i[2]
        m = i[1]
        for _ in range(m):
            new_coins.remove(c1)
        new_coins.append(c2)


    return combine_mults(new_coins, available_coins)

def combine_coins(target, coins, diff, initial_coins, max):

    if initial_coins == None:
        initial_coins = [coins[0]] * (target // coins[0])
    else:
        initial_coins = initial_coins
        diff = 0

    if coins[0] != max:
        current_coin = coins[1]
    else:
        return initial_coins

    final_coins = []

    last_ind = None
    for idx, i in enumerate(initial_coins):
        diff += i
        if diff % current_coin == 0:
            final_coins = final_coins + ([current_coin] * (diff//current_coin))
            last_ind = idx
            diff = 0


    if last_ind and last_ind < len(initial_coins):
        initial_coins = initial_coins[last_ind+1:] + final_coins
    elif last_ind == len(initial_coins):
        initial_coins = final_coins
    elif not last_ind:
        initial_coins = initial_coins



    initial_coins.sort()
    coins = coins[1:]
    return combine_coins(target, coins, diff, initial_coins, max)

def find_fewest_coins(coins, target):
    if target == 0:
        return []
    if target < 0:
        raise ValueError("target can't be negative")
    if min(coins) > target:
        raise ValueError("can't make target with given coins")
    if target in coins:
        return [target]

    for i in coins:
        if i > target:
            coins.remove(i)

    max = coins[-1]
    diff = target % coins[0]
    initial_coins = None

    new_coins = combine_coins(target, coins, diff, initial_coins, max)
    fff = combine_mults(new_coins, coins)
    fff.sort()

    if sum(fff) != target:
        raise ValueError("can't make target with given coins")
    else:
        return fff