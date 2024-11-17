class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Python Palindrome Check
        #Time: O(n) Space: O(n)
        
        s = "".join([i for i in s.lower() if i.isalnum()])
        return s == s[::-1]