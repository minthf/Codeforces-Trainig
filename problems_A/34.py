n = int(input())
soldiers = list(map(int, input().split()))

minimum = 10000
index_i = 0
index_j = 0
for i in range(n):
    if i != n -1:
        if abs(soldiers[i] - soldiers[i + 1]) < minimum:
            minimum = abs(soldiers[i] - soldiers[i + 1])
            index_i = i
            index_j = i + 1
    else:
        if abs(soldiers[0] - soldiers[-1]) < minimum:
            minimum = abs(soldiers[0] - soldiers[-1])
            index_i = n - 1
            index_j = 0


print(index_i + 1, index_j + 1)