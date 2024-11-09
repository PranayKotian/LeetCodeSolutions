class Solution:
    def trap(self, height: List[int]) -> int:
        
        #Three Pass Solution
        #Time: O(3n) Space: O(2n)
        
        leftMax = []
        rghtMax = []
        
        curMax = 0
        for h in height:
            leftMax.append(curMax)
            curMax = max(curMax, h)
        curMax = 0
        for h in height[::-1]:
            rghtMax.append(curMax)
            curMax = max(curMax, h)
        rghtMax = rghtMax[::-1]
        
        water = 0
        for i in range(len(height)):
            if height[i] < leftMax[i] and height[i] < rghtMax[i]:
                water += min(leftMax[i], rghtMax[i])-height[i]
        return water