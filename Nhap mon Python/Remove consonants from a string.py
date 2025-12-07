#Remove consonants from a string
def remove(s):
    a = ''
    for char in s:
        if char in 'aeiouAEIOU':
            a += char
        else: 
            print('No Vowel')
    return a