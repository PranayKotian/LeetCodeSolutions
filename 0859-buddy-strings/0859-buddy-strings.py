class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        #Counters Solution
        #Time: O(s+g) Space: O(s+g)
        
        cs = Counter(s)
        cg = Counter(goal)
        
        if len(s) != len(goal) or cs != cg:
            return False
        
        swaps = []
        for i in range(len(goal)):
            if goal[i] != s[i]:
                swaps.append(i)
        if len(swaps) == 0:
            return any(i>=2 for i in cs.values())
        return len(swaps) == 2
        
        
        
            