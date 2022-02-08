t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0 for x in range(n+1)]
    for i in arr:
        cnt[i] += 1
    ans = 0
    for s in range(2, 2*n+1):
        cur = 0
        for i in range(1, (s+1)//2):
            if s - i > n:
                continue
            cur += min(cnt[i], cnt[s-i])

        if s % 2 == 0:
            cur += cnt[s // 2] / 2
        ans = int(max(ans, cur))
    print(ans)


    