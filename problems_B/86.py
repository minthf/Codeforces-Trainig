n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
r = []
for i in range(n):
    for k in range(n):
        if i == k:
            continue
        if arr[i][0] < arr[k][0] and arr[i][1] < arr[k][1] and arr[i][2] < arr[k][2]:
            r.append(i)
minimum = 1000
ind = 0
for i in range(n):
    if i in r:
        continue
    if arr[i][3] < minimum:
        minimum = arr[i][3]
        ind = i

print(ind + 1)

