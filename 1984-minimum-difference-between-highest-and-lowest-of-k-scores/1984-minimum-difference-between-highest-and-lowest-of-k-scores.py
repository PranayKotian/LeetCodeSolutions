class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        #Solution 1: Sorting
        #Time: O(nlogn) Space: O(1)
        
        nums.sort()
        res = 10**6
        k -= 1
        for l in range(len(nums)-k):
            res = min(res, nums[l+k]-nums[l])
        return res