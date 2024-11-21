class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        '''
        Sort intervals
        Hold a current intervals and interate through the list
        If overlap: remove the interval that ends later
        If no overlap: cur interval == most recently looked at
        '''
        
        #Sort + One Pass Solution
        #Time: O(nlogn) Space: O(1)
        
        intervals.sort()
        res = 0
        s0,e0 = intervals[0]
        for s1,e1 in intervals[1:]:
            if s1 < e0: #overlap
                res += 1
                if e1 < e0:
                    s0,e0 = s1,e1
            else:
                s0,e0 = s1,e1
        return res