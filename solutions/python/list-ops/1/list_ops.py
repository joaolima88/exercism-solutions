def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    res = initial
    for i in list:
        res = function(res, i)
    return res


def foldr(function, list, initial):
    res = initial
    for i in list[::-1]:
        res = function(res, i)
    return res


def reverse(list):
    return list[::-1]
