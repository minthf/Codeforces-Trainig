n = int(input())
arr = []
for i in range(n):
    arr.append(input().split('|'))
found = True

for k, v in enumerate(arr):
    if v[0] == 'OO':
        print('YES')
        found = False
        arr[k][0] = '++'
        break
    elif v[1] == 'OO':
        print('YES')
        found = False
        arr[k][1] = '++'
        break
if found:
    print('NO')
else:
    for i in arr:
        print(i[0] + '|' + i[1])