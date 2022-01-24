t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    summary = 0
    i = 0
    while i < n and summary + arr[i] >= (i + 1) * x:
        summary += arr[i]
        i += 1
    print(i)


