n = int(input())
presents = list(map(int, input().split()))

arr = []
for i in range(1, n + 1):
    arr.append(presents.index(i) + 1)

for i in arr:
    print(i, end=' ')