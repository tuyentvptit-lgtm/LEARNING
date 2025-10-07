a, b, c, d, e =  map(int, input().split())
numbers = [a, b, c, d, e]
cnt = [0]* 1001
found = True
for i in numbers:
    cnt[i] += 1
    if cnt[i] > 1:
        found = True
    else:    
        found = False
if found == True:
    print('NO')
else:
    print('YES')