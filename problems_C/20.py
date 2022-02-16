n = int(input())
s = input()
count = 0
m = 0
found = False
for i in s:
    if i == ')':
        count -= 1
    else:
        count += 1
    m = min(count, m)

if count == 0 and m >= -1:
    print("Yes")
else:
    print("No")