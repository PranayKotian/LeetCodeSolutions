class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #DP Solution
        #Time: O(n^2) Space: O(n)
        
        arr = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], arr[j]+1)
        
        return max(arr)