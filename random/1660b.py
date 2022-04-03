t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    ans = False
    if n == 1:
        if arr[0] > 1:
            print('NO')
        else:
            print('YES')

    else:
        if arr.count(max(arr) - 1) or arr.count(max(arr)) > 1:
            print('YES')
        else:
            print('NO')
