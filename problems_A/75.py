n = int(input())

arr = [[0 for i in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

print(max([max(x) for x in arr]))
