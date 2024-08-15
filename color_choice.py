def checkchoose(m, n):
    def fact(x):
        ans = 1
        for i in range(2, x+1):
            ans *= i
        return ans
    def choose(n, x):
        return fact(n)//(fact(x)*fact(n-x))
    x = 0
    while True:
        if x > n:
            return -1
        result = choose(n, x)
        if result == m:
            return x
        x += 1

# 27593523553342842144
# n = 72
print(checkchoose(27593523553342842144, 72))