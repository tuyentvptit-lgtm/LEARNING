#Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = s.split(" ")
        return len(word[-1])