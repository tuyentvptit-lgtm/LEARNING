n = int(input())
for i in range(n):
    cnt = 0
    a = list(map(int, input().split()))
    for j in range(len(a) - 1):
        if a[j] == a[j - 1]:
            cnt += 1
        else:
            print(min(a), max(a))
            break
    if cnt != 0:
        print('BANG NHAU')
        break