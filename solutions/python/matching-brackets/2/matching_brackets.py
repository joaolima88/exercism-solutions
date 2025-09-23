def remove(string):
    if string == '':
        return True
    if '[]' not in string and '{}' not in string and '()'not in string:
        return False
    else:
        return remove(string.replace('()','').replace('{}','').replace('[]',''))

def is_paired(string):

    string=''.join([i for i in string if i in '([{}])'])

    if not string:
        return True
    if '[]' not in string and '{}' not in string and '()'not in string:
        return False
    if len(string) % 2 != 0:
        return False
    if string[0] in '}])' or string[-1] in '([{':
        return False
    if string[:(len(string)//2)] == string[len(string)//2:][::-1].translate(str.maketrans(')]}', '([{')):
        return True
    else:
        return remove(string)