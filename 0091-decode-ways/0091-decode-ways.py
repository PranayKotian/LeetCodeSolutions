class Solution:
    def numDecodings(self, s: str) -> int:
        #DP Solution
        #Time: O(n) Space: O(1)
        
        validNums = set([str(i) for i in range(1,27)])
        if s[0] not in validNums: 
            return 0
        
        arr = [1,1,0]
        for i in range(1,len(s)):
            if s[i] in validNums:
                arr[2] += arr[1]
            if s[i-1:i+1] in validNums:
                arr[2] += arr[0]
            arr = [arr[1], arr[2], 0]
        return arr[1]