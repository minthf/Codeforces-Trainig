a, b = map(int, input().split())

guys = list(map(int, input().split()))

count = 0

for i in guys:
    if 5 - i >= b:
        count += 1

print(count // 3)
