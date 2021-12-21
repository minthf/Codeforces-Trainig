n = int(input())
s = input()
x = 0
y = 0
count = 0
a = False
for k, i in enumerate(s):
    if i == 'U':
        y += 1
    if i == 'R':
        x += 1
    if x == y:
        if k == len(s) - 1:
            pass
        else:
            if s[k + 1] == i:
                count += 1
print(count)
