def find(letter):
    d = {
    1 : 'AEIOULNRST',
    2 : 'DG',
    3 : 'BCMP',
    4 : 'FHVWY',
    5 : 'K',
    8: 'JX',
    10 : 'QZ'
    }


    for i in d.items():
        if letter in i[1]:
            return i[0]



def score(word):
    s = 0
    for i in [(i.upper(),word.count(i)) for i in set(word)]:
        s += find(i[0]) * i[1]
    return s