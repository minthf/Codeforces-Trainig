t= int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    found = True
    for i in range(n):
        if i + 1 < n and arr[i] == n and arr[i + 1] != 1:
            found = False
        if i + 1 < n and arr[i] == 1 and arr[i + 1] != 2:
            found = False
        if arr.count(n) > 1:
            found = False
        if arr.count(1) > 1:
            found = False
    if found:
        print('YES')
    else:
        print('NO')
