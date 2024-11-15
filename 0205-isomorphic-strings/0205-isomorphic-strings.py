class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #Python Zip Solution
        #Time: O(n) Space: O(n)
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
        
        """
        #Dictionary + Set Solution
        #Time: O(n) Space: O(n)
        
        if len(s) != len(t):
            return False
        
        taken = set()
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                if table[s[i]] != t[i]:
                    return False
            elif t[i] in taken:
                return False
            table[s[i]] = t[i]
            taken.add(t[i])
        return True
        """