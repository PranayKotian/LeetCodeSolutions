#https://leetcode.com/problems/length-of-last-word/
#Title: Length of Last Word
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if (len(words) > 0):
            return len(words[-1])
        return 0