class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        BRUTE FORCE SOLUTION
        count = 0
        
        for i in grid:
            for j in range(len(i) - 1, -1, -1):
                if i[j] < 0:
                    count += 1
                    
        return count
        """ 
        
        
        count = 0
        rows = len(grid) 
        colPos = len(grid[0]) -1 
        
        for i in grid:
            #iterates through rows
            for j in range(colPos, -1, -1):
                if i[j] < 0:
                    count += rows
                    #if neg val is found entire col is elimated cus all vals would be ne
                    colPos -= 1
                else: 
                    #once positive val is hit we know there are no more negative numbers in the row
                    continue
            rows -= 1
        
        return count
