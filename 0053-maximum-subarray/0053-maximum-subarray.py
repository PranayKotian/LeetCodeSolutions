class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Greedy Solution
        #Time: O(n) Space: O(1) 
        
        cur = 0
        res = nums[0]
        for n in nums:
            cur += n
            if cur > res:
                res = cur
            if cur < 0:
                cur = 0
        return res
        
        #Brute Force Solution
        #Time: O(n^2) Space: O(1)