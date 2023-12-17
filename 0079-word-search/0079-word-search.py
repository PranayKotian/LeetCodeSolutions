class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r,c,idx):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[idx]:
                return
            if idx == len(word)-1:
                return True
            
            temp = board[r][c]
            board[r][c] = "0"
            
            p1 = dfs(r+1,c,idx+1)
            p2 = dfs(r-1,c,idx+1)
            p3 = dfs(r,c+1,idx+1)
            p4 = dfs(r,c-1,idx+1)
            
            board[r][c] = temp
            
            return p1 or p2 or p3 or p4
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False