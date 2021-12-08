n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())

a -= 1
b -= 1

years = 0
for i in range(a, b):
    years += d[i]

print(years)