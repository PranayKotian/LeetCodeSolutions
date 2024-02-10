class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        #Solution 1: Non-Constant Space Solution
        #Time: O(n+m) Space: O(n+m)
        
        p1 = p2 = 0
        res = []
        while p1 < len(nums1)-len(nums2) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        res += nums1[p1:len(nums1)-len(nums2)]
        res += nums2[p2:]
        
        for i in range(len(res)):
            nums1[i] = res[i]