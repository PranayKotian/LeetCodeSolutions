class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #Brute force solution
        #Time: O(n^2) Space: O(1)
        
        #Two pass solution
        #Time: O(2n) Space: O(1)
        
        res = nums[0]
        cur = 1
        for n in nums:
            cur *= n
            res = max(res,cur)
            if cur == 0:
                cur = 1
        cur = 1
        for n in nums[::-1]:
            cur *= n
            res = max(res,cur)
            if cur == 0:
                cur = 1
        
        return res