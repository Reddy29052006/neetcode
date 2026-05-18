class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()[::-1];
        count=0;
        for i in s:
            if i==" ":
                return count;
            count+=1
        return count;


        