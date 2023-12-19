class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfsPacific(r,c,prev):
            if r < 0 or c < 0:
                return True
            if r == ROWS or c == COLS or heights[r][c] > prev:
                return False
            if (r,c) in pacific:
                return True
            
            temp = heights[r][c] 
            heights[r][c] = 10**6
            b1 = dfsPacific(r+1,c,temp)
            b2 = dfsPacific(r-1,c,temp)
            b3 = dfsPacific(r,c+1,temp)
            b4 = dfsPacific(r,c-1,temp)
            heights[r][c] = temp
            if b1 or b2 or b3 or b4:
                pacific.add((r,c))
                return True
        
        def dfsAtlantic(r,c,prev):
            if r == ROWS or c == COLS:
                return True
            if r < 0 or c < 0 or heights[r][c] > prev:
                return False
            if (r,c) in atlantic:
                return True
            
            temp = heights[r][c] 
            heights[r][c] = 10**6
            b1 = dfsAtlantic(r+1,c,temp)
            b2 = dfsAtlantic(r-1,c,temp)
            b3 = dfsAtlantic(r,c+1,temp)
            b4 = dfsAtlantic(r,c-1,temp)
            heights[r][c] = temp
            if b1 or b2 or b3 or b4:
                atlantic.add((r,c))
                return True
        
        res = []
        for y in range(ROWS):
            for x in range(COLS):
                if dfsPacific(y,x,10**6) and dfsAtlantic(y,x,10**6):
                    res.append([y,x])

        return res