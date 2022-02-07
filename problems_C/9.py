n, m = map(int, input().split())
arr = []
summary = 0
count = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp[0] - tmp[1])
    summary += tmp[0]

arr = sorted(arr, reverse=True)

i = 0
while summary > m:
    if count >= n:
        count = -1
        break
    summary -= arr[i]
    count += 1
    i += 1

    

print(count)

