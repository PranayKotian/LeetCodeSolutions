class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        #Palindrome Check Solution
        #Time: O(n) Space: O(1)
        
        def is_palindrome(text: str) -> bool:
            return text == text[::-1]
        
        if is_palindrome(s):
            return True
        
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
            l += 1
            r -= 1
        #error