n, k = map(int, input().split())
days = list(map(int, input().split()))
res = 0
for i in range(0, n-1):
    if days[i] + days[i + 1] < k:
        res += k - days[i] - days[i + 1]
        days[i + 1] += k - days[i] - days[i + 1]
if n == 1:
        print(0)
        print(days[0])

else:
    print(res)
    for i in days:
        print(i, end=' ')
    print('')