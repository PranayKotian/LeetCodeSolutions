class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        #Check Swaps Solution
        #Time: O(n) Space: O(1)
        
        if len(s1) != len(s2):
            return False
        
        swap = []
        count = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count == 0:
                    count += 1
                    swap.append(s1[i])
                    swap.append(s2[i])
                elif count == 1:
                    if s1[i] != swap[1] or s2[i] != swap[0]:
                        return False
                    count += 1
                else:
                    return False
        
        if count == 1:
            return False
        return True
        
        """
        #Swap Letters Solution
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
        """