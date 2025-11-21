def chia_het_cho_2(n):
    if n % 2== 0:
        return True
    else:
        return False

n = int(input())
chia_het_cho_2(n)
if chia_het_cho_2(n) == True:
    print(n, 'chia het cho 2')
else:
    print(n, 'ko chia het cho 2')