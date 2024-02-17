class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #Solution 2: Sorting Solution (Optimized)
        #Time: O(nlogn) Space: O(1)
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start,end in intervals[1:]:
            if start < prevEnd:
                res += 1
                if end < prevEnd:
                    prevEnd = end
            else:
                prevEnd = end
        return res
        
        """
        #Solution 1: Sorting Solution
        #Time: O(nlogn) Space: O(1)
        intervals.sort()
        prev = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < prev[1]:
                res += 1
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]
            else:
                prev = intervals[i]
        return res
        """