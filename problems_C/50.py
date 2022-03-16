t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    cnt = [[0, 0] for i in range(n+m-1)]
    for i in range(n):
        for j in range(m):
            cnt[i + j][arr[i][j]] += 1
    ans = 0
    for i in range(n + m - 1):
        j = n + m - 2 - i
        if(i <= j):
            continue;
        ans += min(cnt[i][0] + cnt[j][0], cnt[i][1] + cnt[j][1]);
    print(ans)
