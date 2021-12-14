n = input()

count = 0

for i in n:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
        elif i == '1' or i == '3' or i == '5' or i == '7' or i == '9':
            count += 1

print(count) 