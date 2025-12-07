class Solution:
    def countSort(self,s):
        a = ''
        b = sorted(s)
        for i in range(len(b)):
            a += b[i]
        return a