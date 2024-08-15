def rot(lis, keep):
    n = len(lis)
    # 1 2 3 4 5
    # 2 3 4 5 1
    output = lis[:keep] + lis[keep+1:] + lis[keep:keep+1]
    return output

def max_rot(n):
    lis = list(str(n))
    ma = n
    for i in range(len(lis)-1):
        lis = rot(lis, i)
        print(lis)
        ma = max(ma, int(''.join(lis)))
    return ma

# l = list("12345")
# print(rot(l, 1))
print(max_rot(12345))