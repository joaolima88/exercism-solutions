def initial_basket(basket):
    basket = list(basket)
    size = len(basket)
    groups = []

    while len(basket) > 0:
        g = list(set(basket))
        groups.append(g)

        for i in g:
            basket.remove(i)

    return groups

def new_basket(basket):

    big_group = basket[0]
    small_group = basket[-1]

    if len(big_group) - len(small_group) > 1:

        for i in big_group:
            if i not in small_group:
                small_group.append(i)
                big_group.remove(i)
                return new_basket(sorted(basket,key=len,reverse=True))
    else:
        return basket

def test_different_group_sizes(basket, group_size):
    basket = list(basket)
    x=sorted([[i]*basket.count(i) for i in set(basket)], key=len)
    y=[i for j in x for i in j][::-1]


    groups = []

    while len(y) > 0:
        g=[]
        for i in y:
            if len(g) < group_size:
                if i in g:
                    continue
                else:
                    g.append(i)
            else:
                break
        groups.append(g)
        for i in g:
            y.remove(i)

    return groups

def price(basket):
    size = len(basket)
    discount = {1:0, 2:5, 3:10, 4:20, 5:25}
    return size * (100 - discount[size]) * 8

def total(basket):
    if len(initial_basket(basket)) > 1:

        price_1 = 0
        for i in initial_basket(basket):
            price_1 += price(i)

        price_2 = 0
        for j in new_basket(initial_basket(basket)):
            price_2 += price(j)

        price_3 = 0
        for i in test_different_group_sizes(basket,4):
            price_3 += price(i)

        price_4 = 0
        for i in test_different_group_sizes(basket,3):
            price_4 += price(i)

        return min([price_1,price_2,price_3,price_4])

    else:
        price_1 = 0
        for i in initial_basket(basket):
            price_1 += price(i)
        return price_1