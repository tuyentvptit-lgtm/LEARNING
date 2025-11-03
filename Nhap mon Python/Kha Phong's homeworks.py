n = int(input())
m = list(map(int, input().split()))
k = 0
for i in m:
    if i % 2 != 0:
        k += i
print(k)
