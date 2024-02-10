class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        #Solution 1: Dyanmic Programming
        #Time: O(n^2) Space: O(n^2)
        
        n = len(board)
        flip = 0 #initially false for first row
        newboard = []
        
        for r in range(n-1,-1,-1):
            if flip: newboard += (board[r][::-1])
            else: newboard += (board[r])
            flip ^= 1
        
        minmoves = [21**2 for i in range(n**2)]
        minmoves[0] = 0
        
        def explore(i):
            for j in range(i+1, min(i+7,n**2)):
                if newboard[j] != -1:
                    j = newboard[j]-1
                if minmoves[i]+1 < minmoves[j]:
                    minmoves[j] = minmoves[i]+1
                    explore(j)
        
        for a in range(n**2):
            explore(a)
        
        if minmoves[-1] == 21**2: return -1
        return minmoves[-1]