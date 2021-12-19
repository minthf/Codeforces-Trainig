n = int(input())

for i in range(n):
    a, k = map(int, input().split())
    s = list(map(int, input().split()))
    if min(s) + k >= max(s) - k:
        print(min(s) + k)
    else:
        print(-1)
