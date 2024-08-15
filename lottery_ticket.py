def bingo(ticket,win):
    count = 0
    for string, code in ticket:
        if any(ord(c) == code for c in string):
            count += 1
    if count >= win:
        return "Winner!"
    else:
        return "Loser!"

print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1))