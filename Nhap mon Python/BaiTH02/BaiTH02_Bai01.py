a = input()
print(len(a))
freq = {}
for ch in a:
    freq[ch] = freq.get(ch, 0) + 1

print("Số lần xuất hiện của mỗi ký tự:")
for ch, count in freq.items():
    print(f"'{ch}': {count}")
