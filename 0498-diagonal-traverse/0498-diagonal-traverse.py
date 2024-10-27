class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        #Dictionary Solution
        #Time: O(n) Space: O(n)
        
        table = defaultdict(list)
        
        ROWS = len(mat)
        COLS = len(mat[0])
        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS):
                table[i+j].append(mat[i][j])
        
        res = []
        r = 0
        while r in table:
            if r%2 == 0:
                res += table[r]
            else:
                res += table[r][::-1]
            r += 1
        return res