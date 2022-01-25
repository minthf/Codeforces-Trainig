t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    found = True
    good = [0, 0]
    for i in range(n):
        if (a[i] > b[i] and not good[0]):
            found = False
            print('NO')
            break
        elif (a[i] < b[i] and not good[1]):
            found = False
            print('NO')
            break

        if (a[i] == -1):
            good[0] = 1
        if (a[i] == 1):
            good[1] = 1

    if found:
        print('YES')