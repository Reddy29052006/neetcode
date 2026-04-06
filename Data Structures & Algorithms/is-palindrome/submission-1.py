class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=''
        for i in range(len(s)):
            if s[i].isalnum():
                newS = newS + s[i]
        return newS[::-1].lower() == newS.lower()