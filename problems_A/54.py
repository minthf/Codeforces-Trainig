n = int(input())
a = ''
for i in range(1, n + 1):
    if i % 2 == 0:
        a += 'I love that '
    else:
        a += 'I hate that '

print(a[:-5] + 'it')

