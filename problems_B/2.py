two, three, five, six = map(int, input().split())

summ = 0


if two > 0 and five > 0 and six > 0:
    tmp = min(two, five, six)
    summ += 256 * tmp
    two -= tmp 
    five -= tmp
    six -= tmp
if three > 0 and two > 0:
    tmp = min(two, three)
    summ += 32 * tmp
    two -= tmp
    three -= tmp

print(summ)
