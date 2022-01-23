a, b, c = input().split()
a, b = map(int, (a, b))

arr = []
for i in range(a):
    arr.append(input())

res = []
for i in range(a):
    for j in range(b):
        if arr[i][j] == c:
            if i != 0 and arr[i-1][j] != c and arr[i-1][j] != '.':
                res.append(arr[i-1][j]);
            if i != a-1 and arr[i+1][j] != c and arr[i+1][j] != '.':
                res.append(arr[i+1][j])
            if j != 0 and arr[i][j-1] != c and arr[i][j-1] != '.':
                res.append(arr[i][j-1])
            if j != b-1 and arr[i][j+1] != c and arr[i][j+1] != '.':
                res.append(arr[i][j+1])

print(len(set(res)))