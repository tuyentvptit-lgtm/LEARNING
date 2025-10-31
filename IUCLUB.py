n = input()
ch = ''
for i in n:
    if i not in '123456789':
        ch += i
print(ch)