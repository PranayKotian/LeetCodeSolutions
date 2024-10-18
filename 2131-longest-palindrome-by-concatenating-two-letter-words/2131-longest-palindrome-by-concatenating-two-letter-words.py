class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        #Dictionary Solution
        #Time: O(n) Space: O(n)
        
        table = defaultdict(int)
        for w in words:
            table[w] += 1
        
        res = 0
        center = False
        for k in table:
            if k[0] == k[1]:
                if table[k]%2 == 1:
                    center = True
                res += (table[k]//2)*4
            elif k[::-1] in table:
                res += min(table[k], table[k[::-1]])*2
        if center:
            res += 2
        return res
        