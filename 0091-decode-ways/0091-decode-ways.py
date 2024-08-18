class Solution:
    def numDecodings(self, s: str) -> int:
        
        #Dynamic Programming Solution
        #Time: O(n) Space: O(1)
        
        validNums = set([str(i) for i in range(1,27)])
        if s[0] not in validNums: 
            return 0
        
        arr = [1,1,0]
        for i in range(1,len(s)):
            if s[i] in validNums:
                arr[2] += arr[1]
            if s[i-1]+s[i] in validNums:
                arr[2] += arr[0]
            arr = [arr[1], arr[2], 0]
        return arr[1]
        
        
        """
        #Dynamic Programming Solution - same solution but less clean
        #Time: O(n) Space: O(1)
        
        valid = set([str(i) for i in range(1,27)])
        c1, c2 = 1, 0
        if s[0] in valid:
            c2 = 1
        for i in range(1, len(s)):
            c3 = 0
            if s[i] in valid:
                c3 += c2
            if s[i-1:i+1] in valid:
                c3 += c1
            c1, c2 = c2, c3
        return c2
        """