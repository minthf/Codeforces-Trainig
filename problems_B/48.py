n = int(input())
arr = list(map(int, input().split()))
maxi = max(arr)
ind = arr.index(maxi)
b = True
for i in range(n-1):
    if i < ind:
        if arr[i] > arr[i + 1]:
            b = False
    if i > ind:
        if arr[i] < arr[i + 1]:
            b = False

if b:
    print('YES')
else:
    print('NO')
