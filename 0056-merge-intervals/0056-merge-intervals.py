class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sort + Combine Intervals
        #Time: O(nlogn) Space: O(1)
        
        intervals.sort()
        res = []
        for s1,e1 in intervals:            
            if res and s1 <= res[-1][1]:
                res[-1][1] = max(res[-1][1],e1)
            else:
                res.append([s1,e1])
        return res