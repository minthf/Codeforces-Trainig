n = int(input())
for i in range(n):
    s = input()
    t = input()
    p = input()
    sp = [0] * 26
    tx = [0] * 26
    for i in s + p:
        sp[ord(i)-97] += 1
    for i in t:
        tx[ord(i)-97] += 1
    l = 0
    for i in range(len(t)):
        if t[i] == s[l]:
            l += 1
        if l == len(s): break
    sub = l == len(s)
    if not sub:
        print("NO")
        continue
    for i in range(26):
        if sp[i] < tx[i]:
            print("NO")
            break
    else:
        print("YES")