#Nhập vào n (0<=n<=10^18), in ra số lượng chữ số chẵn, lẻ của n.
#Yêu cầu nhập số bộ test
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    d = 0
    while n > 0:
        d += n % 10
        if n > 0:
            count += 1
        n //= 10
    print(count)