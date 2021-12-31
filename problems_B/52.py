a, b, c = map(int, input().split())

emocii = sorted(list(map(int, input().split())))

f = emocii[-1]
s = emocii[-2]

if b % (c+1) == 0:
    print((f * c + s)* (b // (c+1)))
else:
    print((f * c + s) * (b // (c+1)) + (f * (b % (c+1))))