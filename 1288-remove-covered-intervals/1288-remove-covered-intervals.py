class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        #Brute Force
        #Time: O(n^2) Space: O(1)
        
        res = 0
        n = len(intervals)
        for i in range(n):
            covered = False
            for j in range(n):
                if i == j:
                    continue
                a = intervals[i][0]
                b = intervals[i][1]
                c = intervals[j][0]
                d = intervals[j][1]
                
                if c <= a and b <= d:
                    covered = True
                    break
            if not covered:
                res += 1
        return res