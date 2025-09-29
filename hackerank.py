import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n %i == 0:
            return False
    return True

n = int(input())
if snt(n) == True:
    print('YES')
else:
    print('NO')