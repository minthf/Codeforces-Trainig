n = int(input())

ticket = input()

first = 0
second = 0
lucky = True
for k, v in enumerate(ticket):
    if v not in ['4', '7']:
        lucky = False
        break
    if k < n//2:
        first += int(v)
    else:
        second += int(v)

if not lucky:
    print("NO")
elif first == second:
    print("YES")
else:
    print("NO")
