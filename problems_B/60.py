first_n = int(input())
first_arr = {}
for i in range(first_n):
    a, b = map(int, input().split())
    first_arr[a] = b

second_n = int(input())
second_arr = {}
for i in range(second_n):
    a, b = map(int, input().split())
    second_arr[a] = b

res = 0


for i in first_arr:
    if second_arr.get(i):
        if second_arr.get(i) >= first_arr.get(i):
            pass
        else:
            res += first_arr.get(i)
    else:
        res += first_arr.get(i)
for i in second_arr:
    if first_arr.get(i):
        if first_arr.get(i) > second_arr.get(i):
            pass
        else:
            res += second_arr.get(i)
    else:
        res += second_arr.get(i)

print(res)
