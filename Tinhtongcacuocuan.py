#Tính số ước của n mà <n
import math
def so_uoc(n):
    so_uoc = 0
    for i in range (1, math.isqrt(n) + 1):
        if n %i == 0:
            so_uoc += 2
            if i == n//i:
                so_uoc -= 1 
    return so_uoc

if __name__ == '__main__':
    n = int(input('Nhap so n = '))
    print('Số ước của n = ', so_uoc(n))
