class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        #Two Pointer Solution
        #Time: O(n+m) Space: O(min(m,n))
        
        res = []
        p1 = p2 = 0
        while p1 != len(firstList) and p2 != len(secondList):
            s1,e1 = firstList[p1]
            s2,e2 = secondList[p2]
            
            if s2 > e1:
                p1 += 1
            elif s1 > e2:
                p2 += 1
            else: #overlap
                res.append([max(s1,s2), min(e1,e2)])
                if e1 < e2:
                    p1 += 1
                else:
                    p2 += 1
        return res
                    
        
        """
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
        """