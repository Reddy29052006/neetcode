class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords=set([])

        for i in range(0,len(words)):
            word = words[i]
        
            for j in range (i+1,len(words)):


                if word in words[j]:
                    matchingWords.add(word)
                    
                if words[j] in words[i]:
                    matchingWords.add(words[j])
                    

        return  list(matchingWords)