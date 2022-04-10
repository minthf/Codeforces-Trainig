t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    num = {}
    maximum = arr[0]
    maxv = 1
    for i in arr:
        try:
            num[i] += 1
            if num[i] > maxv:
                maxv = num[i]
                maximum = i
        except KeyError:
            num[i] = 1
    if maxv == n or n == 1:
        print(0)
    else:
        res = maxv
        ans = 0
        while res < n:
            d = min(n - res, res)
            ans += 1 + d
            res += d
        print(ans)


