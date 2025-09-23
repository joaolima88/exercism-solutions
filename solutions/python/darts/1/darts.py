def score(x, y):
    x = x**2
    y = y**2
    if x+y > 100:
        return 0
    if 100 >= x+y > 25:
        return 1
    if 25 >= x+y > 1:
        return 5
    if 1 >= x+y >= 0:
        return 10
