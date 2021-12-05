n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
a = []
for i in range(n):
    a.append(matrix[i][n-1-i])
    for m in range(n):
        if i == m:
            if i != n//2:
                a.append(matrix[i][m])
        if i == n//2:
            if m != n//2:
                a.append(matrix[i][m])
        if m == n//2:
            if i != n//2:
                a.append(matrix[i][m])

print(sum(a))