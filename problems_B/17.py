n = int(input())

b = sorted(list(map(int, input().split())))

l = len(b)

if l % 2 == 0:
    left = b[:l // 2]
    up = b[l // 2:]

else:
    left = b[:l // 2]
    up = b[l // 2:]

print(sum(left)**2 + sum(up)**2)