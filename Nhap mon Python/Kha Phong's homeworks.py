#Nhập vào n (0<=n<=10^18), in ra số lượng chữ số chẵn, lẻ của n.
#Yêu cầu nhập số bộ test
t = int(input())
for i in range(t):
    n = int(input())
    chan = 0
    le = 0
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    print(chan, le)
   