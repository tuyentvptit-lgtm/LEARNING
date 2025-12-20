import random
m = random.randint(1, 10)
while m > 0:
    n = int(input())
    while n != m:
        if n < m:
            print('Nhỏ hơn')
            break
        if n > m:
            print('Lớn hơn')
            break
