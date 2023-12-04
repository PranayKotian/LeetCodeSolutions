#https://leetcode.com/problems/flood-fill/
#Title: 733. Flood Fill
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        oricol = image[sr][sc]
        
        if oricol == newColor:
            return image
        
        def dfs(y,x):
            if y < 0 or x < 0 or y >= h or x >= w or image[y][x] != oricol:
                return
            
            image[y][x] = newColor
            
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
        
        dfs(sr,sc)
        
        return image