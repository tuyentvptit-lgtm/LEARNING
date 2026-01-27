n = list(map(str, input().split()))
m = sorted(n)
a = ''
for i in range(len(m)):
    a += m[i]
    a += ' '
print(a)