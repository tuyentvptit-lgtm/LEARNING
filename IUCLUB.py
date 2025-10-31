n = input()
str = []
for ch in n:
    if ch not in str:
        str.append(ch)
print(len(str))