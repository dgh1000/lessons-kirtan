def one_fold(lis):

    output = [1]
    nex = 0
    for x in lis:
        output.append(x)
        output.append(nex)
        nex = 1-nex
    return output

def compute():
    current = [1]
    while len(current) < 1000000:
        current = one_fold(current)
    return current

def paper_fold():
    l = compute()
    for i in l: yield i

l = compute()
print(len(l))
print(sum(l))
