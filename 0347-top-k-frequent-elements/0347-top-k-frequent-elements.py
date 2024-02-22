class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Solution 1: Python Counter Solution
        #Time: O(n) Space: O(n)
        
        c = Counter(nums)
        c = [i for i,j in c.most_common()][:k]
        return c