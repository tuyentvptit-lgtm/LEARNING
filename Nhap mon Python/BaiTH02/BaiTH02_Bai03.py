a = input()
cnt= 0
for i in range(len(a)):
    if a[i] == 'u' or a[i] == 'e' or a[i] == 'o' or a[i] == 'a' or a[i] == 'i':
        cnt += 1
print(f'Có {cnt} nguyên âm')
print(f'Có {len(a) - cnt} phụ âm')