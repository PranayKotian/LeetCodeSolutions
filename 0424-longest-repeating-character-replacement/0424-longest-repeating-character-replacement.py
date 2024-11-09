class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #Sliding Window Solution
        #Increase window until (window size - count of most common letter ) > k
        #Decrease window until constraint it met
        #Update maxlength each time window size increases
        #Time: O(n) Space: O(n)
        
        count = defaultdict(int)
        l = 0
        res = 0
        for r in range(0,k):
            count[s[r]] += 1
        for r in range(k,len(s)):
            count[s[r]] += 1
            while (r-l+1 - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return max(res,len(s)-l)