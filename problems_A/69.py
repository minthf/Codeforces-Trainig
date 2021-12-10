a, b, c = map(int, input().split())

arr = []
arr.append(a + c + b)
arr.append(a + a + b + b)
arr.append(a + a + c + c)
arr.append(b + b + c + c)

print(min(arr))