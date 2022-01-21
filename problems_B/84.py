n = int(input())
palki = list(map(int, input().split()))
s = set(palki)

res = 0
for i in s:
    tmp = palki.count(i)
    if tmp >= 2:
        res += tmp // 2

print(res // 2)
