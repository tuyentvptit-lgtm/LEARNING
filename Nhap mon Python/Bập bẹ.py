m, x = map(int, input().split())
n = list(map(int, input().split()))
count = 0
left = 0
right = len(n) - 1
for left in range(len(n)):
    for right in range(left + 1, len(n) + 1):
        if sum(n[left:right]) == x:
            count += 1
print(count) 