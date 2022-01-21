n = input()
four = n.count('4')
seven = n.count('7')

if four == 0 and seven == 0:
    print(-1)
elif seven > four:
    print(7)
else:
    print(4)