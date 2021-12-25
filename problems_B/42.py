n = int(input())

tests = list(map(int, input().split()))

for i in tests:
    t = i % 14
    d = i // 14
    if d >= 1 and t in range(1, 7):
        print('YES')
    else:
        print('NO')
