n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j] == max(a):
            a.insert(j, y)
    for i in range(len(a)):
        if a[i] < 0:
            print(a[i], end = ' ')
    for i in range(len(a)):
        if a[i] > 0:
            print(a[i], end = ' ')