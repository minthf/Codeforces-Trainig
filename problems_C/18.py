t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = [-1 for i in range(n+1)]
    ans = n + 5
    for i in range(n):
        if l[arr[i]] != -1:
            ans = min(i - l[arr[i]] + 1, ans)
        l[arr[i]] = i
    if ans > n:
        print(-1)
    else:
        print(ans)