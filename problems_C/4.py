n = int(input())
res = 2
tmp = 2
for i in range(1, n):
    tmp *= 2
    res += tmp

print(res)