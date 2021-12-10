n = int(input())
cake = []

for i in range(n):
    cake.append(input())

count = 0
for i in range(n):
    for k in range(n):
        if cake[i][k] == 'C':
            for j in range(i + 1, n):
                if cake[j][k] == 'C':
                    count += 1
            for j in range(k + 1, n):
                if cake[i][j] == 'C':
                    count += 1

print(count)