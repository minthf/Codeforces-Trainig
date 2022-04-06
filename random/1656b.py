t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    v = sorted(list(map(int, input().split())))
    ans = False
    if n == 1:
        ans = v[0] == k
    else:
        i = 0
        j = 1
        while j < n and i < n:
            if v[i] + abs(k) == v[j]:
                ans = True
                break
            elif v[i] + abs(k) < v[j]:
                i += 1
            else:
                j += 1
    print('YES' if ans else 'NO')
