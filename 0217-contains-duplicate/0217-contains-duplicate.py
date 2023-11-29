class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        #O(n) time and space
        #Ends execution early as soon as duplicate is found
        #Worst case O(n) time and space if no duplicate exists
        cache = set()
        for n in nums:
            if n in cache:
                return True
            else:
                cache.add(n)
        return False