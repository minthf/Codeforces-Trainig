n, ice = map(int, input().split())
arr = []

childrens = 0

for i in range(n):
    n = list(input().split())
    n[1] = int(n[1])
    if n[0] == '+':
        ice += n[1]
    else:
        if ice < n[1]:
            childrens += 1
        else:
            ice -= n[1]

print(ice, childrens)
