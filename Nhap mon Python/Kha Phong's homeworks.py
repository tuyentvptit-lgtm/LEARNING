a, b, c, k =  map(float, input().split())
T = a + b + c
if k == 1:
    d = 0.75
elif k == 2:
    d = 0.5
point = (30 - T)/7.5*d
diem = round(point)
print(diem)
