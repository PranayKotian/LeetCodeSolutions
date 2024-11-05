class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        #Optimal Solution
        # Run path finding and find path that contains the smallest value
        
        n = len(grid)
        speed = [[sys.maxsize for i in range(n)] for j in range(n)]
        visited = set()
        
        def explore(r,c,pathMax):
            if r < 0 or c < 0 or r >= n or c >= n or (r,c) in visited or speed[r][c] <= pathMax:
                return
            pathMax = max(pathMax, grid[r][c])
            speed[r][c] = min(pathMax, speed[r][c])
            
            visited.add((r,c))
            explore(r+1,c,pathMax)
            explore(r-1,c,pathMax)
            explore(r,c+1,pathMax)
            explore(r,c-1,pathMax)
            visited.remove((r,c))
            
        explore(0,0,-1)
        return speed[-1][-1]
    
        #Brute Force Solution
        # Run path finding for all t = 0 to n^2-1 and return when first valid path is found