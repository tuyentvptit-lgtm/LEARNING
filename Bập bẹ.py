n, m = map(int, input().split())
a = []
c = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(n):
    c.append(a[0][i])

for i in range(1, m):
    c.append(a[i][n - 1])
print(c)