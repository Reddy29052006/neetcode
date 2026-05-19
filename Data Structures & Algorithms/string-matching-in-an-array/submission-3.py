class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords=[]

        for i in range(0,len(words)):

            for j in range (i+1,len(words)):
                if words[i] in matchingWords:
                    break
                
                if words[j] in matchingWords:
                    continue

                if words[i] in words[j]:
                    matchingWords.append(words[i])
                    
                if words[j] in words[i]:
                    matchingWords.append(words[j])
                    

        return  matchingWords