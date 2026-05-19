class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords=[]
        words.sort(key=len)

        for i in range(len(words)):
            word = words[i]
            for j in range(i+1, len(words)):
                if word in words[j]:
                    matchingWords.append(word)
                    break

        return matchingWords
                    