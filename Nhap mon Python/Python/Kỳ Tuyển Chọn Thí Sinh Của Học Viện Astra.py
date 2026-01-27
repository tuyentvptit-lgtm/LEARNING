n = int(input())
candidates = []
for i in range(1, n+1):
    name = input().strip()
    point_1 = float(input())
    point_2 = float(input())
    if point_1 > 10 and point_2 > 10:
        point_1 /= 10
        point_2 /= 10
    avr = (point_1 + point_2) / 2
    if avr < 5:
        rank = 'TRUOT'
    elif avr < 8:
        rank = 'CAN NHAC'
    elif avr < 9.5:
        rank = 'DAT'
    else:
        rank = 'XUAT SAC'
    candidates.append((i, name, avr, rank))

candidates.sort(key=lambda x: x[2], reverse=True)

for idx, name, avr, rank in candidates:
    print(f"TS{idx:02d} {name} {avr:.2f} {rank}")