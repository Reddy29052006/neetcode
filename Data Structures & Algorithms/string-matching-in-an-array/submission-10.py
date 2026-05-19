class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords=[]

        for i in range(0,len(words)):
            word = words[i]
            for j in range (i+1,len(words)):
                if word in matchingWords:
                    break
                
                if words[j] in matchingWords:
                    continue

                if word in words[j]:
                    matchingWords.append(word)
                    
                if words[j] in words[i]:
                    matchingWords.append(words[j])
                    

        return  matchingWords