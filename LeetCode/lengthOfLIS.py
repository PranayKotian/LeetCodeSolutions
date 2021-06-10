#https://leetcode.com/problems/longest-increasing-subsequence/
#Title: 300. Longest Increasing Subsequence
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        arr = [1 for _ in range(n)]
        
        maxLen = 1
        for i in range(1, n):
            for j in range (i):
                if (nums[i] > nums[j]):
                    # arr[i] = max(arr[i], 1 + arr[j])
                    # maxLen = max(maxLen, arr[i])
                    
                    if arr[j] + 1 > arr[i]:
                        arr[i] = 1 + arr[j]
                    if arr[i] > maxLen:
                        maxLen = arr[i]
                    
        return maxLen
        
        '''
        O(n^2) solution
        Runtime: 6908 ms, faster than 5.02% of Python3 online submissions for Longest Increasing Subsequence.
        Memory Usage: 14.7 MB, less than 16.70% of Python3 online submissions for Longest Increasing Subsequence.
        
        MAX() significantly eats into runtime
        Runtimes using max(): 6908ms, 4904ms, 5168ms
        Runetimes without using max(): 3256ms, 3212ms
        
        '''