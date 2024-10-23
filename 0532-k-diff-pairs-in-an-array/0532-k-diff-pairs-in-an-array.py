class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        #Sorting + Two Pointer
        #Time: O(n) Space: O(1)
        
        res = 0
        if k == 0:
            bag = defaultdict(int)
            for n in nums:
                if bag[n] == 1:
                    res += 1
                bag[n] += 1
            return res
        else:
            bag = set(nums)
            for n in bag:
                tar = n-k
                if tar in bag:
                    res += 1
            return res