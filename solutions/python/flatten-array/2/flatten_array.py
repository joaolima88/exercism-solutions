def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            result.extend(flatten(item))
    return result