"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sub_or_sup(list_one, list_two):
    counter = 0
    switch = None
    for idx,i in enumerate(list_two):
        if i not in list_one:
            continue
        elif i in list_one:
            if counter == 0:
                switch = True
            if switch == True:
                for i in list_two[idx:]:
                    if i not in list_one:
                        switch = False
                        break
                    elif i in list_one:
                        counter += 1
    return counter >= 2


def sublist(list_one, list_two):


    if list_one == [] and list_two != []:
        return SUBLIST
    elif list_two == [] and list_one != []:
            return SUPERLIST
    else:
        if list_one == list_two:
            return EQUAL

        elif list_one != list_two:
            if len(list_one) < len(list_two):
                return SUBLIST if sub_or_sup(list_one, list_two) else UNEQUAL    
            elif len(list_one) > len(list_two):
                return SUPERLIST if sub_or_sup(list_two, list_one) else UNEQUAL
            else:
                return UNEQUAL