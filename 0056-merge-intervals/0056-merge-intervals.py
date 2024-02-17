class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Solution 2: Sort Intervals w/ Merge Interval Solution
        #Time: O(logn) Space: O(n)
        
        intervals.sort()
        res = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(res[-1][1],end)
            else:
                res.append([start,end])
        return res
        
        """
        #Solution 1: Sort Intervals w/ Insert Interval Solution
        #Time: O(nlogn) Space: O(n)
        
        intervals.sort()
        res = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
            curi = intervals[i]
            if cur[1] < curi[0]:
                res.append(cur)
                cur = curi
            cur = [min(cur[0], curi[0]), max(cur[1], curi[1])]
        res.append(cur)
        return res
        """