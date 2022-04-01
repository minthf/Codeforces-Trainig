t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odd = 0
    even = 0
    ev_od = 0
    one = 0
    for i in range(1, n-1):
        if arr[i] % 2 == 0:
            even += arr[i] // 2
        else:
            if arr[i] > 2:
                ev_od += arr[i] // 2
            else:
                one += 1
            odd += 1
    if (odd == one or odd == 1) and even == 0:
        print(-1)
    else:
        print(even + odd + ev_od)
