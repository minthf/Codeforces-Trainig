n, m = map(int, input().split())

i = 1
while True:
    if i > n:
        i = 1 
    if i > m:
        print(m)
        break
    m -= i
    i += 1
