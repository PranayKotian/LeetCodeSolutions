class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def findPalindromes(cur, i):
            if i == len(s):
                if cur[-1] == cur[-1][::-1]:
                    res.append(cur)
                return
            
            if cur[-1] == cur[-1][::-1]:
                findPalindromes(cur + [s[i]], i+1)
            
            cur[-1] += s[i]
            findPalindromes(cur, i+1)
        
        findPalindromes([s[0]],1)
        
        return res