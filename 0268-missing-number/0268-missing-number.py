class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #Solution 2: Bit Manipulation Solution
        #Time: O(n) Space: O(1)
        
        res = 0
        for n in nums:
            res ^= n
        for n in range(len(nums)+1):
            res ^= n
        return res
        
        """
        #Solution 1: Math Solution
        #Time: O(n) Space: O(1)
        
        n = len(nums)
        total = int((1 + n) * (n/2)) #Sum of arithmetic series
        for i in nums: 
            total -= i
        return total
        
        
        #Solution 0: Bag Solution
        #Time: O(n) Space: O(n)
        
        bag = set([i for i in range(len(nums)+1)])
        for n in nums:
            bag.remove(n)
        return bag.pop()
        """