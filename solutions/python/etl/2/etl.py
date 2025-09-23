def transform(legacy_data):
    di = {letter.lower(): score for score, letters in legacy_data.items() for letter in letters}

    return di
