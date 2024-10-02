class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        #Heaps Solution
        #Time: O(nlogn), Space: O(n)
        
        maxHeap = []
        heapq.heapify(maxHeap)
        
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            height = heights[i] - heights[i-1]
            bricks -= height
            heapq.heappush(maxHeap, -height)
            
            while bricks < 0:
                if ladders == 0:
                    return i-1
                bricks += -1*heapq.heappop(maxHeap)
                ladders -= 1
        return len(heights)-1
        
        """
        #Brute Force Solution
        #Time: O(2^n) Space: 
        #Passed: 11/80
        
        self.reached = 0
        def climb(i, b, l):
            self.reached = max(self.reached,i)
            if i == len(heights)-1:
                return
            
            if heights[i] >= heights[i+1]:
                climb(i+1, b, l)
            else:
                if l != 0:
                    climb(i+1, b, l-1)
                if b >= heights[i+1]-heights[i]:
                    climb(i+1, b-(heights[i+1]-heights[i]), l)
        
        climb(0,bricks,ladders)
        return self.reached
        """