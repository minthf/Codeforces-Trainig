a = input()
b = input()
result = ''

for k, v in enumerate(a):
    if v == b[k]:
        result += '0'
    else:
        result += '1'

print(result)
