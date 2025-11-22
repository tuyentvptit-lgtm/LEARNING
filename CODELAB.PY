n = int(input())
for i in range(n):
    name = input()
    point_1 = float(input())
    point_2 = float(input())
    if point_1 and point_2 > 10:
        point_1 /= 10
        point_2 /= 10
    avr = (point_1 + point_2)/2
    if avr < 5:
        rank = 'TRUOT'
    if 5 <= avr <8:
        rank = 'CAN NHAC'
    if 8 <= avr < 9.5:
        rank = 'DAT'
    if avr >= 9.5:
        rank = 'XUAT SAC'
    print('TS0',n,  name,   round(avr, 2), rank)