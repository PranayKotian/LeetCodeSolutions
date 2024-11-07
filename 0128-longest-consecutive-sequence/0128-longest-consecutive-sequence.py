class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Find Starts Solution
        #Time: O(n) Space: O(n)
        
        numsSet = set(nums)
        starts = set()
        
        for n in nums:
            if n-1 not in numsSet:
                starts.add(n)
        
        res = 0
        for n in starts:
            c = 0
            while n in numsSet:
                c += 1
                n += 1
            res = max(res,c)
        return res