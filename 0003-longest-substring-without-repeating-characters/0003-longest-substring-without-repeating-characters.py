class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Sliding Window Solution
        #Time: O(n) Space: O(n)
        
        res = 0
        l = 0
        bag = set()
        for r in range(len(s)):
            if s[r] not in bag:
                bag.add(s[r])
                res = max(res, r-l+1)
            else:
                while s[l] != s[r]:
                    bag.remove(s[l])
                    l += 1
                l += 1
        return res