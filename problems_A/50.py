n = int(input())
a = input().replace('W', ' ').split()
print(len(a))
for i in a:
    print(len(i), end=' ')
