class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        #Counter Solution Optimized
        #Time: O(n^2) Space: O(n^2)
        
        c1 = Counter([a+b for a in nums1 for b in nums2])
        c2 = Counter([c+d for c in nums3 for d in nums4])
        
        res = 0
        for v1 in c1:
            if -v1 in c2:
                res += c1[v1]*c2[-v1]
        return res
        
        """
        #Counter Solution
        #Time: O(n^3) Space: O(n)
        #TLE - 120/132
        
        c1,c2,c3,c4 = Counter(nums1), Counter(nums2), Counter(nums3), Counter(nums4)
        res = 0
        for v1 in c1:
            for v2 in c2:
                for v3 in c3:
                    tar = -v1-v2-v3
                    if tar in c4:
                        res += c1[v1]*c2[v2]*c3[v3]*c4[tar]
        return res
        
        
        #Brute Force + Dict Solution
        #Time: O(n^3) Space: O(n)
        #TLE - 63/132
        
        nums4dict = {}
        for i,v in enumerate(nums4):
            nums4dict[v] = nums4dict.get(v, 0) + 1
        
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    target = -nums1[i] - nums2[j] - nums3[k]
                    if target in nums4dict:
                        res += nums4dict[target]
        return res
        """