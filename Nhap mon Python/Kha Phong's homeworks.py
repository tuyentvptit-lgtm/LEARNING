import math
a, b = map(int, input().split())
c =  a*a + b*b
def prime(c):
    if c < 2:
            return False
    for i in range(2, math.isqrt(c)+1):
        
        if c % i == 0:
            return False
    return True

if prime(c)== False:
    print('NO')
else:
    print('YES') 