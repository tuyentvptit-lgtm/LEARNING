tuple = (1, 2, 3, 4, 5, 6)
print(tuple[2])
print(tuple[0: 5: 2])
nested_tuple = (1, 2, 3, 4,(5, 6, 7, 8), 9, 10)
print(nested_tuple[3])
print(nested_tuple[4][1])
for i in tuple:
    print (i)
print(len(tuple))
print(tuple.count(1))
#________________________________________________
number_set = {1, 2, 3, 4, 5}
empty_set = set()
number_set.add(6)
number_set.update('7', '8')
for i in number_set:
    if i == 2:
        print(i)
squares = {a**2 for a in range(6)}
print(squares)
test = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10]
print(set(test))