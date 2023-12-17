class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def ordering(cur, leftover):
            if leftover == []:
                res.append(cur)
            
            for i in range(len(leftover)):
                temp = leftover.copy()
                temp.remove(leftover[i])
                ordering(cur+[leftover[i]], temp)
        
        ordering([], nums)
        return res