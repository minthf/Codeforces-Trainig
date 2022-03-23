t = int(input())
for i in range(t):
    s = input()
    c = input()
    found = False
    for i in range(len(s)):
        if s[i] == c and (i+1) % 2 != 0:
            found = True
            break
    if found:
        print('YES')
    else:
        print('NO')


