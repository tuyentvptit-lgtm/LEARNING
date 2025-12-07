x, y, z = map(int, input().split())
count = 0
buoi = x // z + y // z
if x < y and x % z != 0:
    x += 1
    count += 1
elif x > y and y % z != 0:
    y += 1
    count += 1
print(buoi, count)
    
    