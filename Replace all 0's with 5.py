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