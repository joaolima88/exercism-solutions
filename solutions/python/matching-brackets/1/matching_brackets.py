def remove(string):
    list_string = list(string)
    if len(list_string) == 3:
        return False
    elif len(list_string) == 2:
        return True
    else:
        for idx,i in enumerate(list_string):
            if i in '([{':
                if list_string[idx+1] == i.translate(str.maketrans('([{',')]}')):
                    del list_string[idx:idx+2]
        return is_paired(list_string)

def is_paired(string):

    clean_string=''.join([i for i in string if i in '([{}])'])

    if not clean_string:
        return True
    if '[]' not in clean_string and '{}' not in clean_string and '()'not in clean_string:
        return False
    if len(clean_string) % 2 != 0:
        return False
    if clean_string[0] in '}])' or clean_string[-1] in '([{':
        return False
    if clean_string[:(len(clean_string)//2)] == clean_string[len(clean_string)//2:][::-1].translate(str.maketrans(')]}', '([{')):
        return True
    else:
        return remove(clean_string)