class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #Counter Solution
        #Time: O(n) Space: O(n)
        
        res = 0
        c = Counter(nums)
        for n in c:
            if c[n] > 1:
                for i in range(1,c[n]):
                    res += i
        return res