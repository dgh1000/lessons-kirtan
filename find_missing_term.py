def find_missing(sequence):
    d = min(abs(y-x) for x, y in zip(sequence, sequence[1:]))
    for x, y in zip(sequence, sequence[1:]):
        if abs(y-x) > d:
            return (y+x)//2
    return 0

print(find_missing([1, 6, 11, 21]))
