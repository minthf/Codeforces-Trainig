points = int(input()) - 10
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]
count = 0
if points > 11 or points < 0:
    print(0)

else:
    for i in cards:
        if i == points:
            if i == 10:
                count += 15
            else:
                count += 4
    print(count)
