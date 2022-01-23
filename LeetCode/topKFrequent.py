#https://leetcode.com/problems/top-k-frequent-elements
#Title: Top K Frequent Elements
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashtable = {}
        
        for i, val in enumerate(nums):
            hashtable[val] = 0
        for i in range(len(nums)):
            hashtable[nums[i]] = hashtable[nums[i]] + 1
        
        output = []
        for i in range(k):
            max_key = max(hashtable, key=hashtable.get)
            output.append(max_key)
            del hashtable[max_key]

        return output

  		# Runtime: 242 ms, faster than 5.09% of Python3 online submissions for Top K Frequent Elements.
		# Memory Usage: 18.7 MB, less than 85.33% of Python3 online submissions for Top K Frequent Elements.

