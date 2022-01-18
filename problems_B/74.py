n, m = map(int, input().split())
arr = []
for i in range(n):
    t = list(map(int, input().split()))
    arr.append(min(t))

print(max(arr))


