class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Hashmap solution
        #Time: O(n) Space: O(n)
        
        table = {}
        for idx,val in enumerate(nums):
            table[val] = idx
        for idx,n in enumerate(nums):
            tar = target-n
            if tar in table and idx != table[tar]:
                return [idx, table[tar]]
            