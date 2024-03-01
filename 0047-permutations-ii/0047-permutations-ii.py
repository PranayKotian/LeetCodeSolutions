class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #Solution 1: Permutations + Remove Duplicates (Inefficient Solution)
        #Time: O(n^k)   Space: O(n!)
        
        res = []
        def permute(left, cur):
            if left == []:
                if cur not in res: res.append(cur)            
            for n in left.copy():
                left.remove(n)
                permute(left, cur+[n])
                left.append(n)
        
        permute(nums, [])
        return res