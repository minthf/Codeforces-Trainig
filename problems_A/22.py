a = input()

number = a.count('4') + a.count('7')
a = True

for i in str(number):
    if i != '4' and i != '7':
        a = False
        print('NO')
        break

if a:
    print("YES")
