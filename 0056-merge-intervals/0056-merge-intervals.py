class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sort + Combine Intervals
        #Time: O(nlogn) Space: O(1)
        
        intervals.sort()
        res = [intervals[0]]
        for s1,e1 in intervals[1:]:            
            if s1 <= res[-1][1]:
                if e1 > res[-1][1]:
                    res[-1][1] = e1
            else:
                res.append([s1,e1])
        return res