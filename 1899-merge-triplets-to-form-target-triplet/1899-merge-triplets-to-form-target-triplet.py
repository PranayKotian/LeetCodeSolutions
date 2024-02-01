class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Greedy solution (less generalized solution)
        #Time: O(n) Space: O(1) 
        good = set()
        
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i,v in enumerate(trip):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3