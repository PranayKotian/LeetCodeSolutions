class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Dictionary Solution
        #Time: O(n) Space: O(n)
        
        table = {v:i for i,v in enumerate(nums)}
        for i,v in enumerate(nums):
            if target-v in table and table[target-v] != i:
                return [i,table[target-v]]
        return -1 #error