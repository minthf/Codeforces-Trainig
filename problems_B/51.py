a, b = map(int, input().split())

print(min(a - b, b - 1) + 3 * a)
