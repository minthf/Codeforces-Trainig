t = int(input())
for i in range(t):
    n = int(input())
    type = 0
    if (n % 3 == 1):
        type = 1
    else:
        type = 2
    sum = 0;
    while (sum != n):
        print(type, end='')
        sum += type
        type = 3 - type
    print('')