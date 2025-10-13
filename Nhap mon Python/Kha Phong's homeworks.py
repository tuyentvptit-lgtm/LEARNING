a = float(input())
b = float(input())
c = float(input())
dtb = (a + b*2 + c)/4
print(dtb)
if dtb >= 8:
    print('gioi')
elif dtb >= 6.5:
    print('kha banh')
elif dtb >= 5:
    print('trung binh')
else:
    print('yeu')