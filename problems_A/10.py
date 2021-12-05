n, k = map(int, input().split())

scores = list(map(int, input().split()))

positive = -1

for key, v in enumerate(scores):
    if v > 0:
        positive = key

if positive == -1:
    print(0)

elif positive + 1 <= k:
    print(positive + 1)

else:
    count = len(scores) - 1 - scores[::-1].index(scores[k - 1]) + 1 
    print(count)
