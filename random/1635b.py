t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            if i + 2 < n:
                a[i + 1] = max(a[i], a[i + 2])
            else:
                a[i + 1] = a[i]
            
            ans += 1
    print(ans)
    for i in a:
        print(i, end=' ')
    print('')
