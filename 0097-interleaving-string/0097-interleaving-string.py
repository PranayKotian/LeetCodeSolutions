class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Solution 1: Recursive solution with string splicing
        #Time: O(n) Space: O(1?)
        #(where n == len(s3))
        #(Time Limit Exceeded)
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        @lru_cache(None)
        def explore(str1, str2, str3):
            if str1 == "" and str2 == "" and str3 == "":
                return True
            if str1 == "":
                return str2 == str3
            if str2 == "":
                return str1 == str3
            
            p1 = p2 = False
            if str3[0] == str1[0]:
                p1 = explore(str1[1:], str2, str3[1:])
            if str3[0] == str2[0]:
                p2 = explore(str1, str2[1:], str3[1:])
            
            return p1 or p2
        
        return explore(s1, s2, s3)