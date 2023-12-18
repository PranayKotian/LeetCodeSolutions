class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  
        board = [["."]*n for i in range(n)]
        cols = set()
        posDia = set()
        negDia = set()
        
        res = []
        
        def backtrack(r):
            if r == n:
                res.append(["".join(line) for line in board])
                return
            
            for c in range(n):
                if c in cols or r+c in posDia or r-c in negDia:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                
                backtrack(r+1)
                
                board[r][c] = "."
                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
        
        backtrack(0)
        return res