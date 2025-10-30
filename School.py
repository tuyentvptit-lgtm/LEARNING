dict = {
    'Hi': 'Chào',
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}
print(dict['Hi'])
print(dict.get('one'))
print(dict.get('ten', 10))
print(dict.keys())
print(dict.values())
print(dict.items())
school = {
    'cl1': {'num': 45, 'male': 40},
    'cl2': {'num': 50, 'female': 3}
}
print(school['cl1']['male'])