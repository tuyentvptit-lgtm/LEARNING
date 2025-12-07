n = int(input())
a = list (map(int, input().split()))
m = int(input())
b = list (map(int, input().split()))
c = []
A = B = 1
for i in a:
    A *= i
for j in b:
    B *= j
if A < B:
    for i in range(B):
        if A % i == 0 and B % i == 0:
            c.append(i)
if A > B:
    for i in range(A):
        if A % i == 0 and B % i == 0:
            c.append(i)
print(max(c))