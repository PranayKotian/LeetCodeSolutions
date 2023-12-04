#https://leetcode.com/problems/longest-common-prefix/
#Title: Longest Common Prefix
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        PSEUDOCODE
        1. Iterate through the i'th letter of each string
        2. If all the letters are the same, add the letter to the prefix string
        3. Increment i to the next positions
        4. Repeat step 2
        5. Return string once letters are not the same
        '''
        #Checks for empty array of strings
        N = len(strs)
        if(N == 0):
            return ""
        
        #Finds the smallest string to avoid overflow when checking letters
        minLen = len(strs[0])
        for i in strs:
            if (len(i) < minLen):
                minLen = len(i)
        
        prefix = ""
        #Loops through max prefix length
        for i in range(minLen):
            
            #Sets prefix letter to check for
            letter = strs[0][i]
            
            #Loops through all strings in set
            addVal = True
            for j in range(1, len(strs)):
                if not (strs[j][i] == letter):
                    addVal = False
                    break
            
            if (addVal):
                prefix = prefix + letter
            else:
                break
        
        return prefix
                
        