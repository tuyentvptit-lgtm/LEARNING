a = list(map(int, input().split()))
tong = 0
for i in range(len(a)):
    tong += a[i]
avr = tong/len(a)
print(tong)
print(round(avr, 2))
print(max(a))