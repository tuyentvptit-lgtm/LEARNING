import math
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def chan_le(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def min_max(n):
    return min(n), max(n)

if __name__ == '__main__':
    n = int(input())
    if prime(n):
        print(n, 'là snt')
    else:
        print(n, 'không là snt')

    m = list(map(int, input().split()))
    a, b = min_max(m)
    print(a, b)
    if chan_le(a):
        print(a,'la so chan')
    else:
        print(a, 'la so le')
    if chan_le(b):
        print(b, 'la so chan')
    else:
        print(b, 'la so le')