//https://leetcode.com/problems/two-sum/
//Title: Two Sum
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            j = i + 1
            while j < length:
                if target == (nums[i] + nums[j]):
                    return [i, j];
                j += 1