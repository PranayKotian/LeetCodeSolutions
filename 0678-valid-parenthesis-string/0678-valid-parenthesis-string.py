class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMin = 0
        leftMax = 0
        
        for l in s:
            if l == "(":
                leftMin += 1
                leftMax += 1
            if l == "*":
                leftMin = max(0, leftMin-1)
                leftMax += 1
            if l == ")":
                leftMin = max(0, leftMin-1)
                leftMax -= 1
            if leftMax < 0:
                return False
        
        return 0 in range(leftMin,leftMax+1)