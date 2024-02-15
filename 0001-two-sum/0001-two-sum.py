class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Solution 1: Cache Solution
        #Time: O(n) Space: O(n)
        
        cache = {}
        
        for idx,n in enumerate(nums):
            if target-n in cache:
                return [idx, cache[target-n]]
            cache[n] = idx