n = int(input())
m = list(map(int, input().split()))
cnt = 0
a = []
for i in range(len(m)):
    for j in range(1, i):
        if m[j] != m[i]:
            cnt += 1
            a.append(m[j])
print(a)
print(cnt)