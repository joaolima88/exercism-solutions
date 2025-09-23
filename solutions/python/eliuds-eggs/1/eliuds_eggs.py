def egg_count(display_value,re=None):

    if display_value == 0 and re != None:
        re=re[::-1]
        return re.count("1")

    if re is None:
        re = str(display_value%2)
    else:
        re = str(re)
        re += str(display_value%2)

    display_value = int(display_value/2)
    return egg_count(display_value, re)
