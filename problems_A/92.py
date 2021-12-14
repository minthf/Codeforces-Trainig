n = input()

count = 0

for k, v in enumerate(n):
    if v == 'Q':
        for k1, v1 in enumerate(n[k+1:]):
            if v1 == 'A':
                for k2, v2 in enumerate(n[k1+1:]):
                    if v2 == 'Q':
                        
                        if k < k1 + k + 1 < k2 + k1 + 1:
                            count += 1
                    
print(count)
