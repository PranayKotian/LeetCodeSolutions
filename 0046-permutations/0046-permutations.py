class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def ordering(cur, leftover):
            if leftover == []:
                res.append(cur)
            
            for i in range(len(leftover)):
                digit = leftover.pop(0)
                ordering(cur+[digit], leftover)
                leftover.append(digit)
        
        ordering([], nums)
        return res