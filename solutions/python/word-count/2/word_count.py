def count_words(sentence):

    x = "\n\t!?:,;-_&@$%.^"
    y = ' '*len(x)
    table = str.maketrans(x, y)
    final={}
    
    for i in sentence.translate(table).split():
        if i[0] == "'" or i[-1] == "'":
            i = i.lstrip("'").rstrip("'")
            if i.lower() in final:
                final[i.lower()] += 1
            else:
                final[i.lower()] = 1
        else:
            if i.lower() in final:
                final[i.lower()] += 1
            else:
                final[i.lower()] = 1


    if '' in final:
        del(final[''])
    return final