class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, arr):
            leftover = target-sum(arr)
            
            if leftover == 0:
                res.append(arr)
                return
            if leftover < 0 or i == len(candidates):
                return
            
            for n in range(0, leftover//candidates[i]+1):
                backtrack(i+1, arr + [candidates[i]]*n)
        
        backtrack(0, [])
        return res
                