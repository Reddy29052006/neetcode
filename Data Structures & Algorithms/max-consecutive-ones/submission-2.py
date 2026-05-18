class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0

        for i in nums:
            count = (count + 1) * i
            maxi = max(maxi, count)

        return maxi