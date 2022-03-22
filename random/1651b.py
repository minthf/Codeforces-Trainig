er = 10 ** 9
t = int(input())
for i in range(t):
    n = int(input())
    if 3 ** (n - 1) > er:
        print('NO')
    else:
        print('YES')
        q = 1
        for i in range(n):
            print(q, end=' ')
            q *= 3
        print('')

