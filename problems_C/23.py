n = int(input())
arr = sorted(list(map(int, input().split())))
odd = []
even = []
for i in range(n):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd = reversed(odd)
for i in even:
    print(arr[i], end=' ')
for i in odd:
    print(arr[i], end=' ')
print('')