class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def is_palindrome(text: str) -> bool:
            for i in range(len(text)//2):
                if text[i] != text[-(i+1)]:
                    return False
            return True
        
        if is_palindrome(s):
            return 1
        else:
            return 2