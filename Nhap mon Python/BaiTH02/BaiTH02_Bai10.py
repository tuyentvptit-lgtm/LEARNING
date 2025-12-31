a = list(map(int, input().split()))
max_count = 0
num = a[0]  
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count > max_count:
        max_count = count
        num = a[i]