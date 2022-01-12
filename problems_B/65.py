n = int(input())

r = ''
a = 0
b = 0
for i in range(n):
    if i % 2 == 0:
        r += 'aa'
    else:
        r += 'bb'
print(r[:n])

