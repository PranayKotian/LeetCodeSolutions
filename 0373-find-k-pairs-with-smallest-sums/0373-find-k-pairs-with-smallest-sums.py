class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        #Min Heap Solution
        #Time: O(n1 + klogk) Space: O(n1)
        
        #(sum, nums1 index, nums2index)
        minHeap = []
        for i in range(len(nums1)):
            heappush(minHeap, (nums1[i]+nums2[0], i, 0))
        
        res = []
        for i in range(k):
            _, i, j = heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            if j != len(nums2)-1: 
                heappush(minHeap, (nums1[i]+nums2[j+1], i, j+1))
        return res