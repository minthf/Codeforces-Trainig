n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    if a > b: a, b = b, a
    if c > d: c, d = d, c

    if a + c == b and a + c == d:
        print('YES')
    else:
        print('NO')
