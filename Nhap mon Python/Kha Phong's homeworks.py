str = input().strip()
result = ''
for char in str:
    if not char.isdigit():
        result += char
print( result)