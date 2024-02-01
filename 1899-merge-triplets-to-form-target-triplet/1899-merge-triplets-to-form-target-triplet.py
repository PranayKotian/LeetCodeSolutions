class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        #Greedy solution
        #Time: O(n) Space: O(n)
        arr = [0 for i in range(len(target))]
        
        for trip in triplets:
            valid = True
            for i,v in enumerate(trip):
                if v > target[i]:
                    valid = False
            if valid:
                for i,v in enumerate(trip):
                    if v == target[i]:
                        arr[i] = 1

        return sum(arr) == 3
                