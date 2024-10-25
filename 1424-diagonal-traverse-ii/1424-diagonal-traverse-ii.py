class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        #Efficient Diagonal Traversal
        #Time: O(n) Space: O(n)
        
        table = defaultdict(list)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums[i])):
                table[i+j].append(nums[i][j])
        
        c = 0
        res = []
        tot = sum(len(i) for i in nums)
        while len(res) < tot:
            res += table[c]
            c += 1
        return res
        
        
        """
        #Below solutions traverse empty cells making runtime very inefficient
        #Time complexity is much worse than O(n)
        
        #Locate Value in Array Solution
        #Time: O(n) Space: O(1)
        #TLE - 53/56
        
        rows = len(nums)
        c = 0
        res = []
        tot = sum(len(i) for i in nums)
        
        while len(res) != tot:
            for i in range(min(c,rows-1), -1, -1):
                if (c-i) < len(nums[i]):
                    res.append(nums[i][c-i])
            c += 1
        
        return res
        
        
        #Pop from Array Solution
        #Time: O(n) Space: O(n)
        
        rows = len(nums)
        c = 0
        res = []
        
        while not all([i==[] for i in nums]):
            for i in range(min(c,rows-1), -1, -1):
                if nums[i] != []:
                    res.append(nums[i].pop(0))
            c += 1
        
        return res
        """