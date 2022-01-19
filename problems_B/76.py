n = int(input())
mails = input()
if mails.count('1') == 0:
    print(0)
else:
    res = 0
    mails = [x for x in mails.split('0') if x.count('1') >= 1]
    for i in mails:
        res += i.count('1')
    print(res + len(mails) - 1)
