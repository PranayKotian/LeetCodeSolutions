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
        
        if(len(strs) == 0):
            return ""
        
        pos = 0
        cont = True
        string = ""
        while (cont): 
            if (pos > len(strs[0]) - 1):
                break
            letter = strs[0][pos]
            for i in range(len(strs)):
                if (pos == len(strs[i])):
                    cont = False
                    break
                if (strs[i][pos] == letter):
                    cont = True
                else:
                    cont = False
            if (cont == True):
                string = string + letter
                pos = pos + 1
        return string