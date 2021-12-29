n = int(input())
choco = list(map(int, input().split()))
ans = 0
a = choco[-1]
for i in range(n-1, -1, -1):
    if i == n - 1:
        ans += a
    else:
        a = min(a - 1, choco[i])
        if a <= 0:
            break
        ans += a

print(ans)
