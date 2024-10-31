class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        #Backtracking Solution
        #Time: O(9^k) Space: O(k)
        
        res = []
        def backtrack(arr):
            if len(arr) == k:
                if sum(arr) == n:
                    res.append(arr)
                return
            for i in range(arr[-1]+1,10):
                backtrack(arr+[i])
            
        for i in range(1,10):
            backtrack([i])
        return res