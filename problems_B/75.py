n, m = map(int, input().split())
dictionary = []
for i in range(m):
    f, s = input().split()
    if len(f) > len(s):
        dictionary.append([s, f])
    else:
        dictionary.append([f, s])

lect = input().split()

res = ''

for i in lect:
    for k in dictionary:
        if i == k[0] or i == k[1]:
            res += k[0] + ' '

print(res)