t = int(input())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    one = False
    consec = False
    for i in range(n):
        if arr[i] == 1:
            one = True
        if i < n-1 and arr[i]+1 == arr[i+1]:
            consec = True
    if one and consec:
        print('NO')
    else:
        print('YES')