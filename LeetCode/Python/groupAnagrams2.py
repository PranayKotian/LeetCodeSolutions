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
        counters = {}
        index = 0
        
        for i in strs:
            group = str(sorted(i))
            if group not in counters:
                counters[group] = index
                index += 1
                out.append([i])
            else:
                out[counters[group]].append(i)
        
        return out

        """
        Runtime: 104 ms, faster than 48.69% of Python3 online submissions for Group Anagrams.
        Memory Usage: 17.8 MB, less than 54.09% of Python3 online submissions for Group Anagrams.
        """