class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        #Solution 1: Backtracking Solution
        #Time: Space: 
        
        res = []
        def backtrack(arr, start):
            if len(arr) == k:
                res.append(arr)
                return
            for i in range(start, n+1):
                backtrack(arr+[i], i+1)
                
        backtrack([], 1)
        return res