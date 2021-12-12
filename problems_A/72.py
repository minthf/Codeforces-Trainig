price, dollars, quantity = map(int, input().split())

summary = 0

for i in range(1, quantity + 1):
    summary += i*price


if summary - dollars > 0:
    print(summary - dollars)
else:
    print(0)
