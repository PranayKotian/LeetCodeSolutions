#https://leetcode.com/problems/reverse-words-in-a-string-iii/
#Title: 557. Reverse Words in a String III
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def reverseWords(self, s: str) -> str:
        temp =  ""
        ans = ""
        
        for i in s:
            if i == " ":
                ans += temp[::-1] + " "
                temp = ""
            else:
                temp += i
        
        ans += temp[::-1]
        
        return ans