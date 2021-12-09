word = input()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
start = 0
for i in word:
    count += min(abs(start - letters.index(i)), 26 - abs(start - letters.index(i)))
    start = letters.index(i)
print(count)