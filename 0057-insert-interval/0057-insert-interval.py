class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Solution 1: Add As We Go
        #Time: O(n) Space: O(n)
        
        res = []
        start,end = newInterval
        added = False
        
        for i in intervals:
            if added:
                res.append(i)
            elif end < i[0]:
                res.append([start,end])
                res.append(i)
                added = True
            elif start > i[1]:
                res.append(i)
            if start >= i[0] and start <= i[1]:
                start = i[0]
            if end >= i[0] and end <= i[1]:
                end = i[1]
        if not added:
            res.append([start,end])
        
        return res