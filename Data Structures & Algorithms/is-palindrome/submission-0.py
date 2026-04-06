class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newS=''
        for i in range(len(s)):
            if s[i].isalnum():
                newS = newS + s[i]
        return newS[::-1]==newS 