def au(start_verse, end_verse):

    l1 = ['the house that Jack built.',
            'the malt',
            'the rat',
            'the cat',
            'the dog',
            'the cow with the crumpled horn',
            'the maiden all forlorn',
            'the man all tattered and torn',
            'the priest all shaven and shorn',
            'the rooster that crowed in the morn',
            'the farmer sowing his corn',
            'the horse and the hound and the horn']



    l2 = ['that lay in',
        'that ate',
        'that killed',
        'that worried',
        'that tossed',
        'that milked',
        'that kissed',
        'that married',
        'that woke',
        'that kept',
        'that belonged to',
        'This is']

    res = []
    for i, j in zip(l2[: end_verse-1], l1[: end_verse-1]):
        res.insert(0, i + ' ' + j)
    
    return f"This is {l1[end_verse-1]} " + ' '.join(res)

def recite(start_verse, end_verse):

    final = []
    for i in range(start_verse, end_verse+1):
        final.append(au(i,i))

    if final[0] == 'This is the house that Jack built. ':
        final[0] = 'This is the house that Jack built.'

    return final