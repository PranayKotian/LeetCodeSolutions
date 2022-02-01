#https://leetcode.com/problems/longest-consecutive-sequence/
#Title: 128. Longest Consecutive Sequence
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        maxlen = 0
        
        for i in nums:
            if (i - 1) not in numset:
                curlen = 0
                while (i + curlen) in numset:
                    curlen += 1
                maxlen = max(maxlen, curlen)
        
        return maxlen