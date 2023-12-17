class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if sum(candidates) < target:
            return []
        
        candidates.sort()
        
        res = []
        def backtrack(i,arr):
            if sum(arr) == target:
                res.append(arr)
                return
            if i == len(candidates) or sum(arr) > target:
                return
            
            cur = candidates[i]
            backtrack(i+1, arr+[cur])
            while i < len(candidates) and candidates[i] == cur:
                i+=1
            backtrack(i, arr)
        
        backtrack(0,[])
        return res