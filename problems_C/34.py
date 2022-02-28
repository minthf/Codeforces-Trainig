import math
n, m = map(int, input().split())
ans = 0
for i in range(n+1):
    cur = i
    leftn = n - i
    leftm = m - 2 * i

    if leftm >= 0:
        cur += int(min(leftm, leftn // 2))
        ans = int(max(ans, cur))

print(ans)
