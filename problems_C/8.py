a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(list(map(int, input().split())))


for i in range(a-2, 0, -1):
    for j in range(b-2, 0, -1):
        if arr[i][j] == 0:
            arr[i][j] = min(arr[i+1][j], arr[i][j+1]) - 1

summ = 0
for i in range(a):
    if summ == -1:
        break
    for j in range(b):
        if j != b-1:
            if arr[i][j] >= arr[i][j+1]:
                summ = -1
                break 
        summ += arr[i][j]

for i in range(b):
    if summ == -1:
        break
    for j in range(a-1):
        if j != b-1:
            if arr[j][i] >= arr[j+1][i]:
                summ = -1
                break


print(summ)

