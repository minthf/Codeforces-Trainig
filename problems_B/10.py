n = int(input())

for i in range(n):
    s = input()
    ones = s.count('1')
    zeros = s.count('0')
    if min(ones, zeros) % 2 == 0:
        print('NET')
    else:
        print('DA')
