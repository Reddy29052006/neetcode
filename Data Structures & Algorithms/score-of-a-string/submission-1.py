class Solution:
    def scoreOfString(self, s: str) -> int:
        sn=0
        t=ord(s[0])
        for i in s:
            i=ord(i)
            sn += abs(t-i)
            t=i
            
        return sn
        