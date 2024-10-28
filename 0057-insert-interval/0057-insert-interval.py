class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Compact Solution
        #Time: O(n) Space: O(n)
        
        sn,en = newInterval
        res = []
        inserted = False
        
        for s,e in intervals:
            if e < sn:
                res.append([s,e])
            elif s<=sn<=e or s<=en<=e or sn<=s<=en or sn<=e<=en:
                sn = min(sn,s)
                en = max(en,e)
            if s > en: 
                if not inserted:
                    res.append([sn,en])
                    inserted = True
                res.append([s,e])
        
        if not inserted:
            res.append([sn,en])
        
        return res