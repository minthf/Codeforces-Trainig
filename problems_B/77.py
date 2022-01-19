n, m = map(int, input().split())
dela = list(map(int, input().split()))
res = dela[0] - 1
for i in range(1, m):
    if dela[i] >= dela[i-1]:
        res += dela[i] - dela[i-1]
    else:
        res += n - dela[i - 1] + dela[i]
print(res)
