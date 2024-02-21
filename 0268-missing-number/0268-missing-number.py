class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #Solution 1: Math Solution
        #Time: O(n) Space: O(1)
        
        n = len(nums)
        total = int((1 + n) * (n/2)) #Sum of arithmetic series
        for i in nums: 
            total -= i
        return total