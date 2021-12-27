n = int(input())

for i in range(n):
    a = input()
    b = input()
    found = False
    for i in range(len(a)):
        if b.find(a[i]) != -1:
            found = True

    if found:
        print('YES')
    else:
        print('NO')