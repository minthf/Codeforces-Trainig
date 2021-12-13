n = int(input())
result = 0
for i in range(n):
    s = input()
    if "++" in s:
        result += 1
    elif "--" in s:
        result -= 1

print(result)
