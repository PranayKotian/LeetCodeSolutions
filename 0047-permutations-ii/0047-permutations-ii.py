class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #Solution 1: Permutations + Remove Duplicates (Inefficient Solution)
        #Time:      Space: 
        
        res = []
        
        def permute(left, cur):
            if left == []:
                if cur not in res: res.append(cur)
                return
            
            for n in left.copy():
                left.remove(n)
                permute(left, cur+[n])
                left.append(n)
        
        permute(nums, [])
        return res