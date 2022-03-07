t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    res, cur = 0, 1
    for s in a:
        if s * cur >= x:
            res += 1
            cur = 0
        cur += 1
    print(res)