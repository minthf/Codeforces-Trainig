n = int(input())
numbers = input()
a = sorted([int(x) for x in numbers[:n]])
b = sorted([int(x) for x in numbers[n:]])

c1 = 0
c2 = 0

for i in range(n):
    if a[i] > b[i]:
        c1 += 1
    if a[i] < b[i]:
        c2 += 1

if c1 == n or c2 == n:
    print('YES')
else:
    print('NO')
