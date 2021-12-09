a, b = map(int, input().split())

i = 0
q = a
while True:
    if str(q)[-1] == '0' or str(q)[-1] == str(b):
        break
    q += a
    i += 1
print(i + 1)