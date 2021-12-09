n = int(input())

if n % 2 == 0:
    print(n // 2)
    a = '2 ' * (n // 2)
    print(a[:-1])
else:
    print(n // 2)
    print('2 ' * (n // 2 - 1) + '3')