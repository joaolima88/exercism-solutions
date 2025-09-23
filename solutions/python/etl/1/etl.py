def transform(legacy_data):
    
    di={}
    
    for score,letters in legacy_data.items():
        for letter in letters:
            di[letter.lower()]=score

    return di
