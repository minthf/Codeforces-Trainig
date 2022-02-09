t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += max(arr[i] - arr[i + 1], 0)
    print(ans)