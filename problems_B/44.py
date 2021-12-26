c = int(input())
for i in range(c):
    n = int(input())
    rooms = input()
    l = rooms.find('1')
    r = rooms[::-1].find('1')
    if l == -1:
        print(n)
    else:
        print((2  * n) -  (2  *  min(l, r)))
