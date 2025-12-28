a = list(map(int, input().split()))
tong = 0
for i in range(len(a)):
    if a[i] %2 == 0:
        tong += a[i]
print(tong)