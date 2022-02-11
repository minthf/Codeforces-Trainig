t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = []
    b = []
    flag = False
    for i in s:
        if flag:
            if i == '0':
                a.append(0)
                b.append(0)
            if i == '1':
                a.append(1)
                b.append(0)
            if i == '2':
                a.append(2)
                b.append(0)
        else:            
            if i == '0':
                a.append(0)
                b.append(0)
            if i == '1':
                a.append(0)
                b.append(1)
                flag = True
            if i == '2':
                a.append(1)
                b.append(1)
    for i in a:
        print(i, end='')
    print('')            
    for i in b:
        print(i, end='')
    print('')