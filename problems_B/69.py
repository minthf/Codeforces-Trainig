n, a = map(int, input().split())
city = list(map(int, input().split()))

i = a - 2
j = a
left = True
res = 0
while True:
    if i < 0:
        break
    if j >= n:
        left = False
        break
    if city[i] == 1 and city[j] == 1:
        res += 2
    i -= 1
    j += 1

if left:
    res += city[j:].count(1)
else:
    res += city[:i+1].count(1)

if city[a-1] == 1:
    res += 1
print(res)


