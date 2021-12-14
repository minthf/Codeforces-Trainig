n = input()

count = n.count('a')
dlina = len(n)
if count * 2 > dlina:
    print(dlina)
elif count * 2 == dlina:
    print(dlina - 1)
else:
    print(count * 2 - 1)
