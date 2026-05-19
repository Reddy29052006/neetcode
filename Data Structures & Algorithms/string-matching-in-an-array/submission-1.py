class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords=[]

        for i in range(0,len(words)):

            for j in range (i+1,len(words)):
                if (words[i] in words[j]) and (words[i] not in matchingWords):
                    matchingWords.append(words[i])
                    
                if (words[j] in words[i]) and (words[j] not in matchingWords ):
                    matchingWords.append(words[j])
                    

        return  matchingWords