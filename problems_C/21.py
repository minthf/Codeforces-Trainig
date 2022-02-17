t = int(input())
for i in range(t):
    n, m  = map(int, input().split())
    n = n // m
    digits = [((i + 1) * m) % 10 for i in range(10)]
    summary = 0
    for i in range(n % 10):
        summary += digits[i]
    print(summary + n // 10 * sum(digits))