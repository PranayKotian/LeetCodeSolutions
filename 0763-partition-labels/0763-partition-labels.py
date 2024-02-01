class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Greedy solution
        #Time: O(2n) Space: O(26)
        
        lastIdx = {}
        for i,l in enumerate(s):
            lastIdx[l] = i
        
        res = []
        size = 1
        end = lastIdx[s[0]]
        for idx,let in enumerate(s):
            if lastIdx[let] > end:
                end = lastIdx[let]
            if idx == end:
                res.append(size)
                size = 0
            size += 1        
        return res