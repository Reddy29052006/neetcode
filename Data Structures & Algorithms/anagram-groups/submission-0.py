class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            d.setdefault("".join(sorted(s)), []).append(s)

        return list(d.values())