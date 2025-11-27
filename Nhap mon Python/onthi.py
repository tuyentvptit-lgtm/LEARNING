my_tuple = (1,2, 3, 4,(5, 6 , 6), 6, 7, 7, 8)
print(set(my_tuple))
print(my_tuple[4][0])
string = ''
for i in my_tuple:
    string += str(i)
print(string, sep = ' ')
