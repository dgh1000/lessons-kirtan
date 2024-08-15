def find_missing_numbers2(arr):
    output = []
    for x, y in zip(arr,arr[1:]):
        if y > x+1:
            output += range(x+1, y)
    return output

def find_missing_numbers3(arr):
    if len(arr) < 2:
        return []
    s1 = set(arr)
    s2 = set(range(arr[0], arr[-1]+1))
    l = list(s2-s1)
    l.sort()
    return l

def find_missing_numbers(arr):
    if len(arr) < 2:
        return []
    return sorted(
            list(
                set(range(arr[0], arr[-1]+1))
                - set(arr)) )

print(find_missing_numbers([-3,-2,1,4]))
# 1
# 1 | 1 0
# 1 1 0 
# sequence of length n turns into length 2n+1
# 1, 3, 7, 15