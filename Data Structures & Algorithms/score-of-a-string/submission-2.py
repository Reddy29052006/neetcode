class Solution:
    def scoreOfString(self, s: str) -> int:
        sn=0
        t=ord(s[0])
        for i in s:
            sn += abs(t-ord(i))
            t=ord(i)
            
        return sn
        