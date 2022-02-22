a, b = map(int, input().split())
s = input()
st = []
used = [False for x in range(a)]
length = 0
for i in range(a):

    if s[i] == '(':
        st.append(i)
    else:
        used[st[-1]] = True
        used[i] = True
        del(st[-1])
        length += 2
    if length == b:
        break
for i in range(a):
    if used[i] == True:
        print(s[i], end='')
print('')