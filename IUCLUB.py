#Reverse String
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()

#Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = s.split(" ")
        return len(word[-1])
    
#Remove consonants from a string
def remove(s):
    a = ''
    for char in s:
        if char in 'aeiouAEIOU':
            a += char
        else: 
            print('No Vowel')
    return a

#Replace all 0's with 5

def convertFive(n):
    num = ''
    for char in n:
        num += n
        if num == 0:
            num += 5
    return num

n = input()
print(convertFive(n))