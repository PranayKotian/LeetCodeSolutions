#https://leetcode.com/problems/group-anagrams/
#Title: 49. Group Anagrams
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #list of lists of grouped anagrams 
        out = []
        
        #list of Counter groups
        counters = []
        
        for i in strs:
            group = Counter(i)
            if group not in counters:
                counters.append(group)
                out.append([i])
            else:
                out[counters.index(group)].append(i)
        
        return out
    
        """
        Runtime: 1172 ms, faster than 5.02% of Python3 online submissions for Group Anagrams.
        Memory Usage: 20.7 MB, less than 8.15% of Python3 online submissions for Group Anagrams.
        """