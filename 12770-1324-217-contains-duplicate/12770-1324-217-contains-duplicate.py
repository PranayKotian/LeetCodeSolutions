class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for n in nums:
            if n not in cache:
                cache.add(n)
            else:
                return True
        return False