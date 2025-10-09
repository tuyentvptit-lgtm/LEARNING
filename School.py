age = 20
country = 'Chinese'
if age >= 18:
    if country == 'Chinese':
        print('bad guy')
    else:
        print('good guy')
print('Đủ tuổi đi tù')

if age >= 18 and country == 'Chinese':
    print('Người xấu')
else:
    print('Người tốt')

for i in range(1, 101):
    print(i)
sum = 0
for j in range(1, 11):
    sum += j
print(sum)