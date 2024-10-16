class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
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