class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        sp = nums[0]
        fp = nums[nums[0]]
        
        while fp != sp:
            sp = nums[sp]
            fp = nums[nums[fp]]
        
        hp = 0
        while fp != hp:
            hp = nums[hp]
            fp = nums[fp]
        
        return hp