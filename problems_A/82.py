n = int(input())
colors = [x for x in input()]

count = 0
i = 0
while True:
    if i == len(colors) - 1:
        break

    if colors[i] == colors[i + 1]:
        count += 1
        del(colors[i + 1])
    else:
        i += 1

print(count)