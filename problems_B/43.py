n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 1 and b != 1:
        print('NO')
    elif a in [2, 3] and b >= 4:
        print('NO')
    else:
        print('YES')
