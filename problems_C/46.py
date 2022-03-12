t = int(input())
for i in range(t):
    s = input()
    x = int(input())
    n = len(s)
    ns = ['1'] * n
    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                ns[i-x] = '0'
            if i + x < n:
                ns[i+x] = '0'
    rs = []
    for i in range(n):
        if (i - x >= 0 and ns[i - x] == '1') or (i + x < n and ns[i + x] == '1'):
            rs.append('1')
        else:
            rs.append('0')
    if ''.join(rs) == s:
        for i in ns:
            print(i, end='')
        print('')
    else:
        print(-1)
