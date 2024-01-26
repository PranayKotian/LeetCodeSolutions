class Solution:
    def isHappy(self, n: int) -> bool:
        
        explored = set()
        
        while n != 1:
            if n in explored:
                return False
            explored.add(n)
            temp = 0
            for i in str(n):
                temp += int(i)**2
            n = temp
            
        return True