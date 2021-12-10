n = int(input())
cards = list(map(int, input().split()))

summary = sum(cards) / n * 2

for i in range(n):
    for j in range(n):
        if cards[i] + cards[j] == summary and i != j:
            print(i + 1, j + 1)
            cards[i] = 0
            cards[j] = 0
