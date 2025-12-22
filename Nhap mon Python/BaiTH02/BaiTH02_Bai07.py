n = list(map(int, input().split()))
tong = 0
avr = 0
for i in range(len(n)):
    tong += n[i]
    avr = tong/len(n)
print(tong)
print(avr)
print(max(n))
