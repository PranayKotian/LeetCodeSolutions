class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #Fixed Sliding Window
        #Time: O(s1+s2) Space: O(s1)
        
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:s1_len])
        for i in range(s1_len, s2_len):
            if s1_count == s2_count:
                return True
            s2_count[s2[i-s1_len]] -= 1
            s2_count[s2[i]] += 1
        return s1_count == s2_count