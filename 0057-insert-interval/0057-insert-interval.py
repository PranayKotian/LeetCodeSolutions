class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Insert Interval
        #Time: O(n) Space: O(n)
        
        res = []
        s2,e2 = newInterval
        for i in range(len(intervals)):
            s1,e1 = intervals[i]
            if e1 < s2:
                res.append([s1,e1])
                continue
            if s1 > e2:
                return res + [[s2,e2]] + intervals[i:]    
            s2,e2 = min(s1,s2),max(e1,e2)
        return res + [[s2,e2]]
            
            
            
            