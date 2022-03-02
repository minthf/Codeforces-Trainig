n = int(input())
for i in range(n):
    t, k = map(int, input().split())
    s = input()
    tmp = s.split('1')
    if s.count('1') == 0:
        q = (t+k)//(k+1)
        if q == 0:
            print(1)
        else:
            print(q)
    else:
        ans = 0
        for i in range(len(tmp)):
            if i == 0:
                tmp[i] = tmp[i][:-k]
                ans += (len(tmp[i]) + k) // (k+1)
            elif i == len(tmp)-1:
                tmp[i] = tmp[i][k:]
                ans += (len(tmp[i]) + k) // (k+1)
            else:
                tmp[i] = tmp[i][:-k]
                tmp[i] = tmp[i][k:]
                ans += (len(tmp[i]) + k) // (k+1)
        print(ans)
