import math
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    evq = x**2 + y**2
    if x == 0 and y == 0:
        print(0)
    elif math.sqrt(evq) == int(math.sqrt(evq)):
        print(1)
    else:
        print(2)