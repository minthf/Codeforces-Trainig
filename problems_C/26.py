s = input()
n = int(input())
length = 0
for i in s:
    if i != '*' and i != '?':
        length += 1

if length > n and s.count('?') + s.count('*') < length - n:
    print('Impossible')
elif length < n and s.count('*') == 0:
    print('Impossible')
else:
    res = []
    for i in range(len(s)):
        if length != n:
            if length > n:
                if s[i] == '?':
                    del(res[-1])
                    length -= 1
                if s[i] == '*':
                    del(res[-1])
                    length -= 1                
            else:
                if s[i] == '*':
                    res += [s[i-1]] *  (n - length)
                    length += n - length
        if s[i] != '*' and s[i] != '?':
            res.append(s[i])


    print(''.join(res))