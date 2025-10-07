def find(letter):
    d = {
    "1" : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    "2" : ['D', 'G'],
    "3" : ['B', 'C', 'M', 'P'],
    "4" : ['F', 'H', 'V', 'W', 'Y'],
    "5" : ['K'],
    "8": ['J', 'X'],
    "10" : ['Q', 'Z']
    }


    for i in d.items():
        if letter in i[1]:
            return int(i[0])



def score(word):
    s = 0
    for i in [(i.upper(),word.count(i)) for i in set(word)]:
        s += find(i[0]) * i[1]
    return s