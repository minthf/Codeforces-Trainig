n = int(input())
board = [list(input()) for row_id in range(n)]

for i in range(n - 2):
    for j in range(1, n - 1):
        if board[i][j] == '.':
            if board[i + 1][j] == '.' and board[i + 2][j] == '.' and board[i + 1][j-1] == '.' and board[i + 1][j + 1] == '.':
                board[i][j] = '#'
                board[i + 1][j] ='#' 
                board[i + 2][j] = '#'
                board[i + 1][j-1] = '#'
                board[i + 1][j + 1] = '#'


dots = any(row.count('.') for row in board)
if dots:
    print('NO')
else:
    print('YES')
