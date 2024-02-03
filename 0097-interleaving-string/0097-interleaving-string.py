class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Solution 2: Recursive solution (optimized)
        #Time: O(n) Space: O(1?)
        #(where n == len(s3))
        
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l3 != l1 + l2:
            return False
        
        @lru_cache(None)
        def explore(idx1, idx2, idx3):
            if idx1 == l1 and idx2 == l2 and idx3 == l3:
                return True
            
            p1 = idx1!=l1 and s3[idx3] == s1[idx1] and explore(idx1+1, idx2, idx3+1)
            p2 = idx2!=l2 and s3[idx3] == s2[idx2] and explore(idx1, idx2+1, idx3+1)
            return p1 or p2
        
        return explore(0, 0, 0)
        
        """
        #Solution 1: Recursive solution with string splicing
        #Time: O(n) Space: O(1?)
        #(where n == len(s3))
        #(Time Limit Exceeded)
        
        if len(s3) != len(s1) + len(s2):
            return False
        
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
        """