t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    eq = True
    for i in range(n):
        if arr[i] != i + 1:
            if eq:
                ans += 1
            eq = False
        else:
            eq = True
    if ans > 1:
        print(2)
    else:
        print(ans)