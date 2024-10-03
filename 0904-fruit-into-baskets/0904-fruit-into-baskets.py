class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        #Sliding Window Solution
        #Time: O(n), Space: O(1)
        
        l = 0
        f = {}
        res = 0
        
        for r in range(len(fruits)):
            f[fruits[r]] = f.get(fruits[r], 0) + 1
            
            while len(f) > 2:
                f[fruits[l]] -= 1
                if f[fruits[l]] == 0:
                    del f[fruits[l]]
                l += 1
            
            res = max(res, r-l+1)
        
        return res