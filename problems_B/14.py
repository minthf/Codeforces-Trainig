s = int(input())
b = list(map(int, input().split()))
a = []
maximum = 0
for i in range(s):
    if i == 0:
        a.append(b[i])
    else:
        a.append(b[i] + maximum)
    if a[i] > maximum:
        maximum = a[i]

for i in a:
    print(i, end=' ')
print('')
