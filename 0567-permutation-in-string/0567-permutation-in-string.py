class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #Fixed Sliding Window
        #Time: O(s1+s2) Space: O(s1)
        
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        
        s1_count = Counter(s1)
        for i in range(s2_len-s1_len+1):
            if s1_count == Counter(s2[i:i+s1_len]):
                return True
        return False