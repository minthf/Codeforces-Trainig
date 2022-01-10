a,b = map(int, input().split())

pod_s = input()
s = input()
res = []
if s.find(pod_s) != -1:
    print(0)
else:
    for k, v in enumerate(s):
        pos = []
        r = 0
        if k + a - 1 >= b:
            break
        for i in range(a):
            if pod_s[i] != s[k + i]:
                pos.append(i + 1)
                r += 1
        res.append([r, pos])

    res = sorted(res, key=lambda r: r[0])
    print(res[0][0])
    for i in res[0][1]:
        print(i, end=' ')
    print('')
