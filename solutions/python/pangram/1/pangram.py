def is_pangram(sentence):
    x = sentence.upper()
    y = "".join(x.split())
    z = list(set([a for a in y if a.isalpha()]))
    if len(z) == 26:
        return True
    return False