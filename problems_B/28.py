a = input()
b = input()
w = 0
while True:
    i = len(a) - w - 1
    j = len(b) - w - 1
    if i >= 0 and j >= 0 and a[i] == b[j]:
        w += 1
    else:
        break

print(len(a) + len(b) - 2 * w) 