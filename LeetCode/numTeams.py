#https://leetcode.com/problems/count-number-of-teams/   
#Title: Count Number of Teams
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        i = 0
        j = 1
        k = 2
        
        l = len(rating)
        
        count = 0
        
        while (i < (l-2)):
            while (j < (l-1)):
                while (k < l):
                    if (rating[i] < rating[j] and rating[j] < rating[k]):
                        count += 1
                    elif (rating[i] > rating[j] and rating[j] > rating [k]):
                        count += 1
                    
                    k += 1
                
                #Increments j and resets k
                j += 1
                k = j + 1
                
            #Increments i and resets j and k values
            i += 1
            j = i + 1 
            k = j + 1
            
            
        
        '''
        while (i != (l-2)):
            while (k < l):
                if (rating[i] > rating[j]): 
                    #then rating[k] must be less than rating[j]

                    for a in range(k, l):
                        if (rating[k] < rating[j]):
                            count += 1

                elif (rating[i] < rating[j]):
                    #then rating[k] must be greater than rating[j]
                    
                    for a in range(k, l):
                        if (rating[k] > rating[j]):
                            count += 1

                j += 1
                k += 1
            
            i += 1
            j = i + 1
            k = j + 1
        '''
        
        return count