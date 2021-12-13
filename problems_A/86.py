w1, h1, w2, h2 = map(int, input().split())

if w1 == w2:
    print((2*w1) + 2*(h1+h2) + 4)
else:
    print(h1 + h2 + w1 + w2 + h1 +h2 - 1 + (w1-w2) + 5)
