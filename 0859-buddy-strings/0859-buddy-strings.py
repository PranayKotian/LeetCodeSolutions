class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
    
        #Swap First Mismatch Solution
        #Time: O(n) Space: O(1)
        
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(s) != len(set(goal))
        
        first = None
        for i in range(len(s)):
            if goal[i] != s[i]:
                if first is None:
                    first = i
                else:
                    s = list(s)
                    s[i], s[first] = s[first], s[i]
                    s = "".join(s)
                    return s == goal
        return False