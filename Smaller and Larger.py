class Solution:
    def getMoreAndLess(self, arr, target):
        sml = []
        lg = []
        for i in arr:
            if i < target:
                sml.append(i)
            if i > target:
                lg.append(i)
        return(len(sml),len(lg))
