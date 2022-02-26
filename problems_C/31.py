n, q = map(int, input().split())
zad = []
for i in range(q):
    zad.append(list(map(int, input().split())))

serv = [0 for i in range(n)]

for i in zad:
    count = 0
    for j in serv:
        if j <= i[0]:
            count += 1
    if count >= i[1]:
        ans = 0
        tmp = 0
        for j in range(n):
            if serv[j] <= i[0]:
                serv[j] = i[0] + i[2]
                tmp += 1
                ans += j + 1
            if tmp == i[1]:
                break
        print(ans)
    else:
        print(-1)

                

