import math
n = int(input())
for i in range(n):
    m = int(input())
    tong = 0
    result = m
    while m > 0:
        dvi = m % 10
        tong += math.factorial(dvi) 
        m //= 10
    if tong == result:
        print('Yes')
    else:
        print('No')