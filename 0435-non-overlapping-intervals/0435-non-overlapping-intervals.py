class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #Greedy Approach w/ Sorting
        #Time: O(nlogn) Space: O(1)
        
        res = 0
        intervals.sort()
        
        for i in range(1,len(intervals)):
            sp,ep = intervals[i-1]
            sc,ec = intervals[i]
            
            if sc >= ep: #non-overlapping
                continue
            
            res += 1
            if ep < ec:
                intervals[i] = intervals[i-1]
        return res