n, m = map(int, input().split())
found = True
if m > 0:
    dirty = sorted(list(map(int, input().split())))
    if dirty[0] == 1 or dirty[-1] == n:
        print('NO')
        found = False
    elif m > 2:
        for i in range(m - 2):
            if dirty[i] ==  dirty[i + 1] - 1 ==  dirty[i + 2] - 2:
                print('NO')
                found = False
                break

if found:
    print('YES')