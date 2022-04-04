t = int(input())
for i in range(t):
    alpha = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False}
    s = input()
    m = 0
    n = len(s)
    for i in s:
        if alpha[i]:
            m += 2
            alpha = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False}
        else:
            alpha[i] = True
    print(n-m)