def au(start_verse, end_verse):

    l_1 = ["two Turtle Doves,", "three French Hens,", "four Calling Birds,", "five Gold Rings,", "six Geese-a-Laying,", "seven Swans-a-Swimming,", "eight Maids-a-Milking,", "nine Ladies Dancing,", "ten Lords-a-Leaping,",  "eleven Pipers Piping,", "twelve Drummers Drumming,"]

    l_2 = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    res= []

    for i in l_1[:end_verse-1]:
        res.insert(0, i)
        
    if start_verse == 1 and end_verse == 1:
        res.append("a Partridge in a Pear Tree.")
    else:
        res.append("and a Partridge in a Pear Tree.")

    return f"On the {l_2[start_verse-1]} day of Christmas my true love gave to me: " + ' '.join(res)

def recite(start_verse, end_verse):

    final = []
    for i in range(start_verse, end_verse+1):
        final.append(au(i,i))
    return final