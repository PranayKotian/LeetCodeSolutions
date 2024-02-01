class Solution:
    def checkValidString(self, s: str) -> bool:
        
        #Greedy solution
        #Time: O(n) Space: O(2)
        leftMin = 0
        leftMax = 0
        
        for l in s:
            if l == "(":
                leftMin += 1
                leftMax += 1
            if l == "*":
                leftMin -= 1
                leftMax += 1
            if l == ")":
                leftMin -= 1
                leftMax -= 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0