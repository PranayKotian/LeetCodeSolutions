class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #Solution 2: Hashmap Permutations
        #Time: O(n^k) Space: O(n!)
        #where n = number of unique elms in nums
        
        l = len(nums)
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        def permute(cur):
            if len(cur) == l:
                res.append(cur)
            for k in count:
                if count[k] == 0:
                    continue
                count[k] -= 1
                permute(cur+[k])
                count[k] += 1
        permute([])
        return res
        
        """
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
        """