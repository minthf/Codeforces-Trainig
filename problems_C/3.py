n = int(input())
posl = sorted(list(map(int, input().split())), reverse=True)
vozr = []
vozr.append(posl[0])
ub = []
count = 0
found = True
for i in range(1, n):
    if posl[i] == posl[i - 1]:
        count += 1
        ub.append(posl[i])
    else:
        count = 0
        vozr.append(posl[i])
    if count == 2:
        print('NO')
        found = False
        break

if found:
    print('YES')
    print(len(ub))
    for i in ub[::-1]:
        print(i, end=' ')
    print('')
    print(len(vozr))
    for i in vozr:
        print(i, end=' ')
    print('')