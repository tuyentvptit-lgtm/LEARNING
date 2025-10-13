t = int(input())
for _ in range(t):
    n = input().strip()
    print(sum(int(ch) for ch in n))
