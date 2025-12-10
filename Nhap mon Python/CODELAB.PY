import math
n = int(input())
tong = 0
for i in range(n):
    m = int(input())
    while m >0:
        m %= 10
        tong += math.factorial(m)
        m //= 10
    if tong == m:
        print('Yes')
    else:
        print('No')