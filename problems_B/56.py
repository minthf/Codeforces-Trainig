n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
u = [False for x in range(n+1)]

pos = 0

for i in range(n):
    x = b[i]
    if u[x]:
        print(0, end=' ')
        continue
    cnt = 0
    while True:
        cnt += 1
        u[a[pos]] = True
        if a[pos] == x:
            break
        pos += 1
    pos += 1
    print(cnt, end=' ')
