def proverb(*input_data, qualifier):
    r = []
    counter = 0
    while counter+1 < len(input_data):
        r.append(f"For want of a {input_data[counter]} the {input_data[counter+1]} was lost.")
        counter += 1
    if input_data:
        r.append(f"And all for the want of a {qualifier + ' ' + input_data[0] if qualifier else input_data[0]}.")
        return r
    return r