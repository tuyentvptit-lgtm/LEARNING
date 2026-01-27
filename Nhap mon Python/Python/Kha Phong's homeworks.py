a = list(map(int, input().split()))
chan = []
so = ''
tong = 0
for i in a:
    if i % 2 == 0:
        chan.append(i)
        tong += i
for i in chan:
    so += str(i) + ' '
print(so)
print(tong)
avr = tong / len(chan)
print(round(avr, 2))