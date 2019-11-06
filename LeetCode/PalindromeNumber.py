//https://leetcode.com/problems/palindrome-number/submissions/
//Title: Palindrome Number
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[len(str(x))::-1]:
            return True
        else:
            return False