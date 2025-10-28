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
class Solution:
    def convertFive(self, n):
        n = str(n)
        num = ''
        for ch in n:
            if ch == '0':
                num += '5'
            else:
                num += ch
        return int(num)