import sys
t = int(input())
for i in range(t):
    n = int(input())
    arr = sys.stdin.readline().split()
    er = False
    odd = 0
    even = 0
    for i in arr:
        q = int(i)
        if er:
            break
        if q % 2:
            if odd and q < odd:
                er = True
            odd = q
        else:
            if even and q < even:
                er = True
            even = q
    if er:
        print('NO')
    else:
        print('YES')


