class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Find Starts Solution
        #Time: O(n) Space: O(n)
        
        numsSet = set(nums)
        res = 0
        for n in nums:
            if n-1 not in numsSet:
                count = 0
                while n in numsSet:
                    count += 1
                    n += 1
                res = max(res,count)
        return res