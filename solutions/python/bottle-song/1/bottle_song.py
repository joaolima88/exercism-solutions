def au(start):

    n_bottles = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

    number = n_bottles[start-1]
    next_number = n_bottles[start-2].lower()

    if next_number == "one":
        word1, word2  = "bottles", "bottle"
    elif number == "One":
        word1, word2, next_number  = "bottle", "bottles", 'no'
    else:
        word2 = word1 = "bottles"

    return [
            number + " green " + word1 + " hanging on the wall,", 
            number + " green " + word1 + " hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be " + next_number + " green " + word2 + " hanging on the wall."
            ]


def recite(start, take=1):
    res = []
    for i in range(take):
        res.extend(au(start))
        start -= 1
        res.append("")
    return res[0:-1]