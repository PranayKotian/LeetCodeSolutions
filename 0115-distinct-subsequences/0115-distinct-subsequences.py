class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        #Solution 2: Recursive w/ caching
        #Time: Space:
        
        cache = {}
        def backtrack(s1,t1):
            if t1 == "":
                return 1
            if s1 == "":
                return 0
            if (s1,t1) in cache:
                return cache[(s1,t1)]
            
            if s1[0] != t1[0]:
                res = backtrack(s1[1:],t1)
            else:
                res = backtrack(s1[1:],t1[1:]) + backtrack(s1[1:],t1)
            cache[(s1,t1)] = res
            return res
        
        return backtrack(s,t)
        
        """
        #Solution 1: Recursive solution
        #Time: O(2^n) Space: O(n)
        #(Time Limit Exceeded 51/65 passed)
        
        if t == "":
            return 1
        if s == "":
            return 0
        
        if s[0] != t[0]:
            return self.numDistinct(s[1:],t)
        else:
            return self.numDistinct(s[1:],t[1:]) + self.numDistinct(s[1:],t)
        """