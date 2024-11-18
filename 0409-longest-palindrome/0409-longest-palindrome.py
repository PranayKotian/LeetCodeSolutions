class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        #Counter Solution
        #Time: O(n) Space: O(n)
        
        middle = 0
        cnt = Counter(s)
        res = 0
        for val in cnt.values():
            if val%2 == 1:
                middle = 1
            res += (val//2) * 2
        return res + middle