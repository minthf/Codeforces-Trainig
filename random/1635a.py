t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in arr:
        ans |= i
    print(ans)