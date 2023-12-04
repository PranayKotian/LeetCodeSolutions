#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Title: Longest Substring Without Repeating Characters
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ""
        maxLen = 0
        
        for i in range(len(s)):
            tempStr = s[i]
            for j in range(i+1, len(s)):
                if (s[j] not in tempStr):
                    tempStr += s[j]
                else:
                    break
            if (len(tempStr) > maxLen):
                maxLen = len(tempStr)
                
        return maxLen

        '''
        Runtime: 432 ms, faster than 16.83% of Python3 online submissions for Longest Substring Without Repeating Characters.
		Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
        '''