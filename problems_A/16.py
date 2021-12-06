n = int(input())

soldiers = list(map(int, input().split()))

maximum = soldiers.index(max(soldiers))

minimum = len(soldiers) - 1 - soldiers[::-1].index(min(soldiers))

if maximum == 0 and minimum == len(soldiers)-1:
    print(0)
else:
    if maximum > minimum:
        print(maximum - minimum + len(soldiers) - 2)
    else:
        print(maximum - minimum + len(soldiers) - 1)