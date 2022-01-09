n = int(input())
s = input()
x = 0
y = 0
for i in s:
    if i == 'U':
        x += 1
    if i == 'D':
        x -= 1
    if i == 'L':
        y -= 1
    if i == 'R':
        y += 1
print(n - (abs(x) + abs(y)))
