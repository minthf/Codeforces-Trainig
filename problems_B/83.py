n = input()
s = n.split('><')
s[0] = s[0][1:]
s[-1] = s[-1][:-1]
h = 0
for i in s:
    if i[0] != '/':
        print(2 * h * ' ' + '<' + i + '>')
        h += 1
    else:
        h -= 1
        print(2 * h * ' ' + '<' + i + '>')
        