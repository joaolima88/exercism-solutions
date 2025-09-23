def abbreviate(words):
    words = ''.join([i for i in words.replace('-', ' ') if i.isalpha() or i in '- '])
    acronym = words[0]
    for idx, i in enumerate(words):
        if i == ' ':
            acronym += words[idx+1].upper()

    return acronym.replace(' ', '')
