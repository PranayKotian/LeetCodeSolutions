class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sort + Combine Intervals
        #Time: O(nlogn) Space: O(1)
        
        intervals.sort()
        cur = intervals[0]
        res = []
        
        for i in range(1,len(intervals)):
            s1,e1 = cur
            s2,e2 = intervals[i]
            
            if s2 > e1:
                res.append(cur)
                cur = intervals[i]
            else:
                cur = [s1,max(e1,e2)]
        res.append(cur)
        return res