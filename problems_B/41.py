n = int(input())

priz = 0
for i in range(n, 0, -1):
    priz += 1/i

print(f'{priz:.{12}f}')
