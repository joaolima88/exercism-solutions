def rect_dim(text_len):
    res = []

    c1, r1 = 1, 1
    c2, r2 = 1, 0

    while r1 * c1 < text_len:
        c1 += 1
        r1 += 1
    res.append((c1,r1))

    while r2 * c2 < text_len:
        c2 += 1
        r2 += 1
    res.append((c2,r2))

    return sorted(res)[0][0]



def cipher_text(plain_text):
    plain_text = ''.join([i.lower() for i in plain_text if i.isalnum()])
    r = []
    c = rect_dim(len(plain_text))

    for i in range(0, len(plain_text), c):
        r.append(plain_text[i:i+c] + ' ' * (c - len(plain_text[i:i+8])))

    code = []
    ind = 0

    while len(code) < c:
        phrase = ''
        for i in r:
            phrase += i[ind]
        code.append(phrase)
        ind += 1

    return ' '.join(code)
