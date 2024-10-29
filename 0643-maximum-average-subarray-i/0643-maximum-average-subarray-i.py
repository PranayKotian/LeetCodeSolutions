class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #Two Pass Solution
        #Time: O(n) Space: O(1)
        
        cur = sum(nums[:k])
        res = cur
        for i in range(k, len(nums)):
            cur += nums[i]-nums[i-k]
            res = max(res, cur)
        
        return res/k