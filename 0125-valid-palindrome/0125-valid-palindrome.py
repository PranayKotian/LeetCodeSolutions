class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Python Palindrome Check
        #Time: O(n) Space: O(n)
        
        s = s.lower()
        s = "".join([i for i in s if i.isalpha() or i.isnumeric()])
        return s == s[::-1]