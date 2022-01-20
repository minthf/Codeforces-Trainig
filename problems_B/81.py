PI = 3.1415926536
n = int(input())
okr = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(n):
    if i % 2 == 0:
        res += okr[i] ** 2 * PI
    else:
        res -= okr[i] ** 2 * PI

print(res)