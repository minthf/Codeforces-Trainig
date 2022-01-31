t = int(input())
for i in range(t):
    n = int(input())
    s = (n - 1) // 2
    summary = 0
    for i in range(1, s + 1):
        summary += i * i
    print(summary * 8)
        