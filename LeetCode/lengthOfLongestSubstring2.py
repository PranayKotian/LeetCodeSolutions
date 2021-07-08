#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Title: Longest Substring Without Repeating Characters
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #SLIDING WINDOW METHOD
        substr = set()
        
        n = len(s)
        if (n == 0):
            return 0
        
        p1 = 0
        substr.add(s[p1])
        p2 = 1
        res = 1
        
        while p1 < n and p2 < n:
            while s[p2] in substr:
                substr.remove(s[p1])
                p1 += 1 
            substr.add(s[p2])
            p2 += 1
            res = max(res, p2 - p1)
        
        return res