n, k = map(int, input().split())
way = input()
if way.index('T') < way.index('G'):
    way = way[::-1]
i = way.index('G')
while True:
    if i > len(way) - 1:
        print('NO')
        break
    if way[i] == '#':
        print('NO')
        break
    if way[i] == 'T':
        print('YES')
        break
    i = i + k 
