n = int(input())

s = input().replace(' ', '')
maximum = max([len(x) for x in s.split('0')])
tmp = 0
if s[0] == '1' and s[-1] == '1':
    tmp = len(s.split('0')[0]) + len(s.split('0')[-1])

print(max(tmp, maximum))
