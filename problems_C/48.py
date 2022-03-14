t = int(input())
for i in range(t):
        a = input()
        ans=0
        for i in range(10):
            for j in range(10):
                tm=0;
                for k in a:
                    if(tm%2==0 and int(k)==i):
                        tm += 1
                    elif (tm%2!=0 and int(k)==j):
                        tm += 1
                if(i!=j and tm%2!=0):
                    tm -= 1
                ans=max(ans,tm);
        print(len(a) - ans)