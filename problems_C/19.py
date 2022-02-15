t = int(input())
for i in range(t):
    c, m, x = map(int, input().split())
    d = max(c, m) - min(c, m)
    x += d
    if(c > m):
        c -= d
    else:
        m -= d
    ans = min(c, m, x)
    c -= ans
    m -= ans
    x -= ans
    ans += (c + m) // 3
    print(ans)