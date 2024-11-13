class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        #Brute Force Solution
        #Time: O(m*n) Space: O(min(m, n))
        #Compare all intervals from list1 to list2
        
        res = []
        for s1,e1 in firstList:
            for s2,e2 in secondList:
                if e2 < s1:
                    continue
                if s2 > e1:
                    break
                res.append([max(s1,s2), min(e1,e2)])
        return res