t = int(input())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    left = arr[0]
    right = 0
    found = False
    if n % 2 == 0:
        q = n//2
    else:
        q = n//2 + 1
    for i in range(1, q):
        if right > left:
            found = True
            break
        left += arr[i]
        right += arr[-i]
    if right > left:
        found = True
    if found:
        print('YES')
    else:
        print('NO')
