t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    s = sum(arr)
    if m == 0:
        print(0)
    elif m*2 <=s:
        print(1)
    else:
        print(2 * m - s)