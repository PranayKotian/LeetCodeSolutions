class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Double Bag Solution? 
        #O(2n) space, O(n) time
        bag = set(nums)
        starts = set()
        
        for i in nums:
            if i-1 not in bag:
                starts.add(i)
        
        maxVal = 0
        for i in starts:
            length = 1
            while i+length in bag:
                length += 1
            maxVal = max(length, maxVal)
        
        return maxVal
    
        """
        #Bag Solution
        #Time: O(n) Space: O(n)
        
        res = 0
        bag = set(nums)
        for n in nums:
            if n-1 not in bag:
                i = 1
                while n+i in bag:
                    i += 1
                res = max(res,i)
        return res
        """