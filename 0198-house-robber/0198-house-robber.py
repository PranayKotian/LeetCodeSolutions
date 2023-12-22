class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0] + nums
        maxProfit = nums.copy()
        for i in range(2, len(maxProfit)):
            maxProfit[i] = max(maxProfit[i-2] + nums[i], maxProfit[i-1])
        
        return maxProfit[-1]