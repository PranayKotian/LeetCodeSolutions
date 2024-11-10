class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        #MinHeap + MaxHeap Solution
        #Time: O(n) Space: O(k + n)
        
        minHeap = []
        maxHeap = []
        for r in range(len(nums)):
            heappush(minHeap, (nums[r][0], r, 0))
            heappush(maxHeap, (-nums[r][0], r, 0))
        
        #smallest range
        res = [minHeap[0][0], -maxHeap[0][0]]
        
        while True:
            val,row,idx = heappop(minHeap)
            if idx == len(nums[row])-1:
                break
            heappush(minHeap, (nums[row][idx+1], row, idx+1))
            heappush(maxHeap, (-nums[row][idx+1], row, idx+1))
            
            if (-maxHeap[0][0]-minHeap[0][0]) < (res[1]-res[0]):
                res = [minHeap[0][0], -maxHeap[0][0]]
        return res
        
        
        """
        #Sliding Window Solution
        #Time: O(nlogn) Space: O(n)
        #TLE - 92 / 94
        #Solution doesn't leverage the rows already being in sorted order
        
        ROWS = len(nums)
        arr = []
        for r in range(ROWS):
            for c in range(len(nums[r])):
                arr.append([nums[r][c], r])
        arr.sort()
        
        included = {i:0 for i in range(ROWS)}
        smallestRange = [arr[0][0],arr[-1][0]]
        l = 0
        
        '''
        loop through all values
        add included row
        all rows accounted for?
            minimize range on left end
            compare to current smallest range and replace if smaller
        repeat
        '''
        
        for r in range(len(arr)):
            included[arr[r][1]] += 1
            
            if all(i>0 for i in included.values()):
                while included[arr[l][1]] > 1:
                    included[arr[l][1]] -= 1
                    l += 1
                if arr[r][0]-arr[l][0] < smallestRange[1]-smallestRange[0]:
                    smallestRange = [arr[l][0], arr[r][0]]
        return smallestRange
        """