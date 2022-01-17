n, k = map(int, input().split())
index = list(map(int, input().split()))

for i in range(1, n+1):
    if k - i <= 0:
        print(index[k - 1])
        break
    else:
        k -= i