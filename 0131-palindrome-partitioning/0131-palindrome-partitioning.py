class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def findPalindromes(cur, i):
            if i == len(s):
                res.append(cur)
                return
            
            for j in range(i,len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    findPalindromes(cur+[temp], j+1) 
            
        findPalindromes([],0)
        
        return res