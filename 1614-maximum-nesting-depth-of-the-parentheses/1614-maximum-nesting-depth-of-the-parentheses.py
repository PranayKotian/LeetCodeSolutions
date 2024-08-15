class Solution:
    def maxDepth(self, s: str) -> int:
        
        #Greedy Solution
        #Time: O(n) Space: O(1)
        count = 0
        res = 0
        for c in s:
            if c == "(": 
                count += 1
                res = max(res, count)
            if c == ")":
                count -= 1
        return res
        