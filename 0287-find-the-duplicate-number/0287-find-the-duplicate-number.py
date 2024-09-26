class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #Floyd's Algorithm
        #Time: O(n) Space: O(1)
        
        start = 0
        fast = nums[nums[0]]
        slow = nums[0]
        
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        while start != fast:
            start = nums[start]
            fast = nums[fast]
        
        return start
        