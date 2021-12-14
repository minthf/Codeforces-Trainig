n = int(input())

for i in range(n):
    s = int(input())
    if s % 4 == 0:
        print('YES')
        chet = []
        nechet = []
        for i in range(1, s + 1):
            if i % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)
        nechet[-1] += s // 2
        for i in chet + nechet:
            print(i, end=' ')
        print('')
    else:
        print('NO')
