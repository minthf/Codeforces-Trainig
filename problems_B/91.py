f = open('input.txt')
a, b = map(int, f.readline().split())
questions = list(map(int, f.readline().split()))
f.close()
f = open('output.txt', 'w')
i = b - 1
while True:
    if i >= a:
        i = 0
    if questions[i] == 1:
        f.write(str(i + 1))
        break
    i += 1