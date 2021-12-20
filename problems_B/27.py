n = int(input())
arr = []
maximum = 0
for i in range(n):
    a, b = map(int, input().split())
    if maximum < a + b:
        maximum = a + b

print(maximum)

