a, b = map(int, input().split())
numb = sorted(list(set(map(int, input().split()))))
for i in range(b):
    if i >= len(numb):
        print(0)
    else:
        if i == 0:
            print(numb[0])
        else:
            print(numb[i] - numb[i - 1])
        