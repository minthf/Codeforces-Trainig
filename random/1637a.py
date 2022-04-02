t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr == sorted(arr):
        print('NO')
    else:
        print('YES')