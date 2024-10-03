class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #Counter Solution
        #Time: O(n) Space: O(n)
        
        res = 0
        c = Counter(nums)
        for i in c:
            if c[i] > 1:
                n = c[i]-1
                res += int((n/2)*(n+1))
        return res