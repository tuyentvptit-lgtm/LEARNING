def max_num(x, y, z):
    if x >y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > y and z > x:
        return z

x = int(input())
y = int(input())
z = int(input())
max = max_num(x, y ,z)
print('Số lớn nhất trong 3 số là: ', max) 