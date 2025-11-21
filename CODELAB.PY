n = input().strip()
cnt = 0

while len(n) > 1:
    s = 0
    for digit in n:
        s += int(digit)
    n = str(s)
    cnt += 1

print(cnt)
