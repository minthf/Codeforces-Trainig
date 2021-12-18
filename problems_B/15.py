n = int(input())

for i in range(n):
    s = int(input())
    summary = s
    while s >= 10:
        tens = s // 10
        ost = s % 10
        s = ost + tens
        summary += tens


    print(summary)