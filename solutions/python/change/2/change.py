def xx(target, coins, memo = []):
    r=[]
    if coins == []:
        memo.sort(key=lambda x: len(x))
        return memo

    max = len(coins)-1

    while sum(r) < target and max >= 0:
        n = coins[max]
        if (sum(r) + n) <= target:
            r.append(n)
        else:
            max = max- 1
    else:
        memo.append(r)
        return xx(target, coins[:-1], memo)

def yy(x,c,target):
    if not c:
        return x

    diff = target - sum(x)
    r = []
    ind = 0
    current_coin = c[0]


    for i in range(len(x)-1):
        s = sum(x[:ind])
        if (s + diff) % current_coin == 0 and ind !=0:
            x =  x[ind:] + [current_coin] * ((s + diff) // current_coin)
            diff = 0
            c = c[1:]
            return yy(x,c,target)
        else:
            ind += 1
    else:
        c = c[1:]
        return yy(x,c,target)

def find_fewest_coins(coins, target):
    if target == 0:
        return []
    if target < 0:
        raise ValueError("target can't be negative")
    if min(coins) > target:
        raise ValueError("can't make target with given coins")
    if target in coins:
        return [target]

    coins = list(filter(lambda x: target > x, coins))
    final = sorted(xx(target, coins, memo = []), key = len)

   
    if sum(final[0]) == target:
        return sorted(final[0])
    else:
        real_final = yy(final[-1],coins,target)
        real_final.sort()
        if sum(real_final) != target:
            raise ValueError("can't make target with given coins")
        else:
            return real_final