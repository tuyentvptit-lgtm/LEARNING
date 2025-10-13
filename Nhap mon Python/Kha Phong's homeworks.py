a, b, c = map(int, input().split())
if a + b > c and a +c > b and b + c >a:
    if a!= b and b != c and c != a:
        print('YES')
    else:
        print('NO')
else:
    print('NO')