class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        
        n = len(isConnected)
        
        def dfs(row):
            if row in visited:
                return
            
            visited.add(row)
            for c in range(n):
                if isConnected[row][c]:
                    dfs(c)
        
        for r in range(n):
            if r in visited:
                continue
            provinces += 1
            dfs(r)
        
        return provinces