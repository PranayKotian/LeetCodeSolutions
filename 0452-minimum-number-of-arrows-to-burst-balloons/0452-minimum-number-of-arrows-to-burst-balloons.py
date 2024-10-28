class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        #Sorting Solution
        #Time: O(nlogn) Space: O(n)
        
        points.sort()
        res = 1
        a,b = points[0]
        for i in range(1,len(points)):
            c,d = points[i]
            if a<=c<=b:
                b = min(b,d)
            else:
                res += 1
                a,b = c,d
        return res