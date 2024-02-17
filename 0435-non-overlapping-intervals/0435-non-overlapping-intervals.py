class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #Solution 1: Sorting Solution
        #Time: O(nlogn) Space: O(n)
        intervals.sort()
        prev = 0
        res = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                res += 1
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
            else:
                prev = i
        return res