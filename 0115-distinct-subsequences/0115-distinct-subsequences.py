class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def distinct_subsequences(s_idx, t_idx):
            if t_idx == len(t):
                return 1
            if s_idx == len(s):
                return 0
            
            res = 0
            if s[s_idx] == t[t_idx]:
                res += distinct_subsequences(s_idx+1, t_idx+1)
            res += distinct_subsequences(s_idx+1, t_idx)
            return res
            
        return distinct_subsequences(0,0)