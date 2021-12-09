n = int(input())
chess = input()

if chess.count('A') > chess.count('D'):
    print('Anton')
elif chess.count('A') < chess.count('D'):
    print('Danik')
else:
    print('Friendship')
