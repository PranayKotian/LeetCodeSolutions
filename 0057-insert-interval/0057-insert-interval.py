class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        sn,en = newInterval
        res = []
        inserted = False
        
        for s,e in intervals:
            if e < sn:
                res.append([s,e])
            elif (s<=sn<=e and s<=en<=e): #interval to insert is in existing interval
                inserted = True
                res.append([s,e])
            elif sn<=s<=en and sn<=e<=en: #existing interval is in interval to insert
                continue
            elif sn<=s<=en:
                en = e
            elif sn<=e<=en:
                sn = s
            if s > en: 
                if not inserted:
                    res.append([sn,en])
                    inserted = True
                res.append([s,e])
        
        if not inserted:
            res.append([sn,en])
        
        return res