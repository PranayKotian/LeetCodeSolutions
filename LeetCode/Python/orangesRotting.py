#https://leetcode.com/problems/rotting-oranges/
#Title: 994. Rotting Oranges
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        steps = 0
        fresh = 0
        queue = []

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 2:
                    queue.append([y,x])
                if grid[y][x] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            for a in range(len(queue)):
                y,x = queue.pop(0)
                
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ny = y + i
                    nx = x + j
                    if (ny<0 or nx<0 or ny>=h or nx>= w) or grid[ny][nx] != 1:
                        continue
                    grid[ny][nx] = 2
                    queue.append([ny, nx])
                    fresh -= 1
            steps += 1
                
        return steps if fresh == 0 else -1