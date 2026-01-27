n = int(input())
for i in range(n):
    ma = input().strip()
    ten = input().strip()
    gioVao = float(input())
    gioRa = float(input())
    tongPhut = int((gioRa - gioVao) * 60)
    gio = tongPhut // 60
    phut = tongPhut % 60
    print(f"{ma} {ten} {gio} gio {phut} phut")