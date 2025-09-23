def sum_of_multiples(limit, multiples):
    m = set()
    for i in multiples:
        if i==0:
            return sum(m)
        else:
            mult = 1
            while i * mult < limit:
                m.add(i * mult)
                mult += 1
    return sum(m)