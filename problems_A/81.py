ii = 0
for i in range(5):
    tmp = list(map(int, input().split()))
    if 1 in tmp:
        j = tmp.index(1)
        ii = i

count = 0
if ii > 2:
    count += ii - 2
elif ii < 2:
    count += 2 - ii


if j > 2:
    count += j - 2
elif j < 2:
    count += 2 - j
print(count)
