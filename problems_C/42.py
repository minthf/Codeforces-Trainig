t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] < arr[n-1]:
        print('YES')
    else:
        print('NO')
