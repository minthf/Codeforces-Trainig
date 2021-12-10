n = int(input())

arr = []

for i in range(n):
    a = input().split()
    arr.append([a[0], int(a[1]), int(a[2])])
found = True
for i in arr:
    if i[1] >= 2400 and i[2] > i[1]:
        found = False
        break

if found:
    print('NO')
else:
    print('Yes')
