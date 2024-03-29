class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Bit manipulation solution
        #Time: O(n) Space: O(1)
        res = 0
        for n in nums:
            res ^= n
        return res