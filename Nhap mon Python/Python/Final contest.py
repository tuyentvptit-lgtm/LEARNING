n = int(input())
a = list(map(int, input().split()))
m = -10**9
tong = 0
for i in range(len(a)):
    tong = max(tong + a[i], a[i])
    m = max(m ,tong)
    
print(m)
