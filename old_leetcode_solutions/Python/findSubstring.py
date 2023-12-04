#https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#Title: Substring with Concatenation of All Words
#Difficulty: Hard
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        #Length of each word in list
        N = len(words[0])
        i = 0
        
        arr = []
        
        while (i < len(s)):
            if (s[i:i+(N-1)] in words):
                arr.append(i)
                i = i + N
                
                #Goes through all following substrings
                while(s[i:i+(N-1)] in words):
                    i = i + N
        return arr

        #TIME LIMIT EXCEEDED