a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] == 6:
        if a[i] != 6 and a[i] != 8:
            if a[i] != 8 and a[i + 2] != 8:
                print('YES')
            elif a[i] == 8 and a[i + 2] != 8:
                print('YES')
    else:
                print('NO')