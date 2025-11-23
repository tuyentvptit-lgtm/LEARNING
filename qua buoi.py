x, y, z = map(int, input().split())
count = 0
if x % z != 0 and y % z != 0 and x < y:
    x += 1
    y -= 1
    count += 1
    print((y // z) + (x // z), count)
elif x % z != 0 and y % z != 0 and x > y:
    x -= 1
    y += 1
    count += 1
    print((x // z) + (y // z), count)
    
    