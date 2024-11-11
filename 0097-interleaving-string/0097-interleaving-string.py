class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        #Brute Force Approach w/ Caching
        '''
        identify the next required letter in s3:
        if next letter in s1: try it
        if next letter in s2: try it
        if neither: return False
        '''
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def search(i1: int, i2: int, i3: int):
            if i3 == len(s3):
                return True
            if i1 == len(s1): 
                return (s3[i3] == s2[i2]) and search(i1,i2+1,i3+1)
            if i2 == len(s2):
                return (s3[i3] == s1[i1]) and search(i1+1,i2,i3+1)
            if s3[i3] != s1[i1] and s3[i3] != s2[i2]:
                return False
            
            res = False
            if s3[i3] == s1[i1]: res = res or search(i1+1,i2,i3+1)
            if s3[i3] == s2[i2]: res = res or search(i1,i2+1,i3+1)
            return res
        
        return search(0,0,0)