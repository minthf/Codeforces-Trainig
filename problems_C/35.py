n = int(input())
for i in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    b = sorted(arr)
    minimum = b[0]
    k = 0
    for i in range(t):
        if(arr[i] != b[i] and arr[i] % minimum > 0):
            k = 1;

    if k:
        print('NO')
    else:
        print('YES')
