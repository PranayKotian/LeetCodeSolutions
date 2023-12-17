class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, arr):
            if sum(arr) == target:
                res.append(arr)
                return
            if sum(arr) > target:
                return
            
            for j in range(i, len(candidates)):
                backtrack(j, arr + [candidates[j]])
        
        backtrack(0, [])
        return res
                