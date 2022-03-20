t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    sq = 0
    dl = s // (n**2)
    ost = n - (n * dl)
    if ost > n:
        dl += 2
    elif ost < n and ost > 0:
        dl += 1
    print(dl)