class MedianFinder:

    def __init__(self):
        self.half1 = [] #maxHeap (negative minHeap)
        self.half2 = [] #minHeap 

    def addNum(self, num: int) -> None:
        if not self.half1:
            heappush(self.half1, -num)
        elif num < -1*self.half1[0]:
            heappush(self.half1, -num)
        else:
            heappush(self.half2, num)
            
        if len(self.half2) > len(self.half1) + 1:
            heappush(self.half1, -1*heappop(self.half2))
        if len(self.half1) > len(self.half2) + 1:
            heappush(self.half2, -1*heappop(self.half1))

    def findMedian(self) -> float:
        h1 = len(self.half1)
        h2 = len(self.half2)
        
        if h1 > h2:
            return -1*self.half1[0]
        elif h2 > h1:
            return self.half2[0]
        return (-1*self.half1[0] + self.half2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()