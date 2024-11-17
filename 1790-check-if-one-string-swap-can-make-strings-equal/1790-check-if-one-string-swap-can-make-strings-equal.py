class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        #Find First Swap Solution
        #Time: O(n) Space: O(1)
        
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        first = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if first is None:
                    first = i
                else:
                    s1 = list(s1)
                    s1[i], s1[first] = s1[first], s1[i]
                    return "".join(s1) == s2
        return False