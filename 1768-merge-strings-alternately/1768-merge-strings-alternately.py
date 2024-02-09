class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        p1 = p2 = 0
        l1 = len(word1)
        l2 = len(word2)
        while p1 < l1 and p2 < l2:
            res += word1[p1]+word2[p2]
            p1 += 1 
            p2 += 1
        if p1 < l1:
            res += word1[p1:]
        if p2 < l2:
            res += word2[p2:]
        return res