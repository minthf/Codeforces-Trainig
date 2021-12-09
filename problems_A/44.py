lemons = int(input())
apples = int(input())
pear = int(input())
found = False
for i in range(lemons, 0, -1):
    if i * 2 <= apples and i * 4 <= pear:
        found = True
        break    

if found:
    print(i + i *2 + i * 4)
else:
    print(0)