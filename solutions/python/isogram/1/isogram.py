def is_isogram(s):
    return len(list([a for a in set(s.lower()) if a.isalpha()])) == len([a for a in s if a.isalpha()])

