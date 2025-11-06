def transpose(text):
    if not text:
        return ''

    lines = text.split('\n')
    max_len = max(map(len, lines))
    padded_lines = [line.ljust(max_len, '*') for line in lines]
    transposed = [''.join(column).rstrip('*') for column in zip(*padded_lines)]

    return '\n'.join(transposed).replace('*', ' ')