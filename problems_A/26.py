n = int(input())
words = []
for i in range(n):
    words.append(input())

for k, v in enumerate(words):
    if len(v) > 10:
        print(v[0] + str(len(v) - 2) + v[-1])
    else:
        print(v)
