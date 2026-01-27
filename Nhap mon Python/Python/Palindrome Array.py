from typing import List
class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        arr_ = arr[::-1]
        if arr == arr_:
            return True
        else:
            return False