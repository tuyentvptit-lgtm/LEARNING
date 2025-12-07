n = list(map(int, input().split()))
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]
print(n)
