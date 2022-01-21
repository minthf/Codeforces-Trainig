n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    a, b = map(int, input().split())
    if b > 0:
        arr1.append([a, b])
    else:
        arr2.append([a, b])

res = 0
count = 1


for i in arr1:
    count += i[1] - 1
    res += i[0]

for i in sorted(arr2, reverse=True):
    if count <= 0:
        break
    count -= 1
    res += i[0]

print(res)