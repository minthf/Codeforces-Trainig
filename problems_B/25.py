n = int(input())

for i in range(n):
    s = input()
    if len(set(s)) == 1:
        print(-1)
    else:
        print(''.join(sorted(s)))
