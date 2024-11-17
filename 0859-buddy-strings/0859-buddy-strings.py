class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        #Count Swaps Solution
        #Time: O(s+g) Space: O(s+g)
        
        if s == goal:
            return any(i>=2 for i in Counter(s).values())
        if Counter(s) != Counter(goal):
            return False
        
        swaps = []
        for i in range(len(goal)):
            if goal[i] != s[i]:
                swaps.append(i)
        return len(swaps) == 2