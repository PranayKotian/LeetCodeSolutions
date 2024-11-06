class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #One Pass Solution
        #Time: O(n) Space: O(1)
        
        res = ~sys.maxsize
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            res = max(res,tot)
            if tot < 0:
                tot = 0
        return res
        
        #Brute Force Solution
        #Time: O(n^2) Space: O(1)