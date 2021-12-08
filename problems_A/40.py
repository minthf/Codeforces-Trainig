n = int(input())
citizen = list(map(int, input().split()))
maximum = max(citizen)
summary = 0
for i in citizen:
    summary += maximum - i
print(summary)
