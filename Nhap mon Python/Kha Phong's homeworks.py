# Ngày tháng năm sinh của An
a, b, c = map(int, input().split())
#Ngày tháng năm sinh của ny An
d, e, f = map(int, input().split())
if c < f:
    print("1")
elif c == f and b < e:
    print("1")
elif c == f and b == e and a < d:
    print("1")
else:
    print('2')