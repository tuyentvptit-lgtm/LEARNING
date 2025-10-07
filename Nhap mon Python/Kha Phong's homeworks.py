expr = input().strip()
left, right = expr.split('=')
left = left.strip()
right = right.strip()
if eval(left) == int(right):
    print(10)
else:
    print(0)
