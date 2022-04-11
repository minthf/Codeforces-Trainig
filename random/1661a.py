t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a1 = []
    b1 = []
    for i in range(n):
        if a[i] > b[i]:
            b1.append(a[i])
            a1.append(b[i])
        else:
            b1.append(b[i])
            a1.append(a[i])
    ans = 0
    for i in range(n-1):
        ans += abs(a1[i] - a1[i+1])
        ans += abs(b1[i] - b1[i+1])
    print(ans)