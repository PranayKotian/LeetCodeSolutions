class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Greedy One Pass
        #Time: O(n) Space: O(1) 
        
        maxSum = nums[0]
        cur = 0
        for n in nums:
            cur += n
            maxSum = max(maxSum, cur)
            if cur < 0:
                cur = 0
        return maxSum