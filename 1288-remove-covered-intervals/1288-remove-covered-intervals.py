class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        #Sorting Solution
        #Time: O(nlogn) Space: O(n)
        
        intervals.sort(key=lambda i:(i[0],-i[1]))
        
        res = 1
        c,d = intervals[0]
        for i in range(1,len(intervals)):
            a,b = intervals[i]
            
            if c <= a and b <= d:
                continue
            else:
                res += 1
                c,d = a,b
        return res
        
        """
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
        """