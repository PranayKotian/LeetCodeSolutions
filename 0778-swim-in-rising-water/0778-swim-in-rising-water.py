class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        #Dijkstra's Algorithm
        #Time: O(n^2 log(n)) Space: O(n^2)
        
        n = len(grid)
        visit = set((0,0))
        minHeap = [(grid[0][0], 0, 0)] #dist, row, col
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while minHeap:
            t,r,c = heappop(minHeap)

            if r == n-1 and c == n-1:
                return t
            
            for dr,dc in dirs:
                neiR, neiC = r+dr, c+dc
                if neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR,neiC) in visit:
                    continue
                visit.add((neiR,neiC))
                heappush(minHeap, (max(grid[neiR][neiC], t), neiR, neiC))
        
        return -1 #error
        
        """
        #Single DFS
        #Time: O(4^(n^2)) Space: O(n^2)
        
        n = len(grid)
        speed = [[sys.maxsize for i in range(n)] for j in range(n)]
        visited = set()
        
        def dfs(r,c,pathMax):
            if r < 0 or c < 0 or r >= n or c >= n or (r,c) in visited or speed[r][c] <= pathMax:
                return
            pathMax = max(pathMax, grid[r][c])
            speed[r][c] = min(pathMax, speed[r][c])
            
            visited.add((r,c))
            dfs(r+1,c,pathMax)
            dfs(r-1,c,pathMax)
            dfs(r,c+1,pathMax)
            dfs(r,c-1,pathMax)
            visited.remove((r,c))
            
        dfs(0,0,-1)
        return speed[-1][-1]
        
        
        #DFS Solution
        #Time: O(n^4) Space: O(n^2)
        #TLE - 21/43 Passed
        
        n = len(grid)
        minTime = n+n-2
        maxTime = n**2
        visited = set()
        
        def dfs(r,c,t):
            if r < 0 or c < 0 or r >= n or c >= n or (r,c) in visited or grid[r][c] > t:
                return False
            if r == n-1 and c == n-1:
                return True
            visited.add((r,c))
            res = dfs(r+1,c,t) or dfs(r-1,c,t) or dfs(r,c+1,t) or dfs(r,c-1,t)
            visited.remove((r,c))
            return res
        
        for time in range(minTime, maxTime):
            if dfs(0,0,time):
                return time
        return -1 #error
        """