class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Compacter Solution
        #Time: O(n) Space: O(n)
        
        sn,en = newInterval
        res = []
        
        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            
            if e < sn:
                res.append([s,e])
            elif s > en: 
                res.append([sn,en])
                return res + intervals[i:]
            else:
                sn = min(sn,s)
                en = max(en,e)
        
        res.append([sn,en])
        return res