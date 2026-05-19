class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords = [ word for i, word in enumerate(words)
    if any(word in other for j, other in enumerate(words) if i != j)]

        return matchingWords
                    