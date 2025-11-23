n = list(map(int, input().split()))
x = int(input())
count = 0
for i in range(len(n)):
    for j in range(i, len(n)):
        if sum(n[i:j+1]) == x:
            count += 1  