class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lens=len(s)
        for i in range(lens - 1, -1, -1):
            if s[i] == " ":
                return lens-i-1
            
        return lens