#UCLN, BCNN
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    x = a * b // gcd(a, b)
    return x
a, b = map(int, input().split())
print('UCLN của a, b = ',gcd(a, b))
print('BCNN của a, b = ', lcm(a, b))