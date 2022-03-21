t = int(input())
for i in range(t):
    s = input()
    r = 0
    g = 0
    b = 0
    R = 0
    G = 0
    B = 0
    for i in range(6):
        if  s[i] == 'r':
            r = i
        elif  s[i] == 'g':
            g = i
        elif  s[i] == 'b':
            b = i

        elif  s[i] == 'R':
            R = i

        elif  s[i] == 'G':
            G = i

        elif  s[i] == 'B':
            B = i
    if R < r or B < b or G < g:
        print('NO')
    else:
        print('YES')