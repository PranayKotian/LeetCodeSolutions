class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Solution 1: Add As We Go
        #Time: O(n) Space: O(n)
        
        res = []
        added = False
        
        for i in intervals:
            if added:
                res.append(i)
            elif newInterval[1] < i[0]:
                res.append(newInterval)
                res.append(i)
                added = True
            elif newInterval[0] > i[1]:
                res.append(i)
            if newInterval[0] >= i[0] and newInterval[0] <= i[1]:
                newInterval[0] = i[0]
            if newInterval[1] >= i[0] and newInterval[1] <= i[1]:
                newInterval[1] = i[1]
        if not added:
            res.append(newInterval)
        
        return res