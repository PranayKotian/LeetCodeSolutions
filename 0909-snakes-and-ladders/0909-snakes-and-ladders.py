class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        #Solution 1: BFS (Shortest Path Problem)
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
        
        visit = set([0])
        q = deque([0])
        
        while q:
            for i in range(len(q)):
                i = q.popleft() 
                for j in range(i+1, min(i+7,n**2)):
                    if newboard[j] != -1: j = newboard[j]-1
                    if j not in visit: q.append(j)
                    minmoves[j] = min(minmoves[j], minmoves[i]+1)
                    visit.add(j)
                    if j == n**2-1: return minmoves[j]
        
        return -1