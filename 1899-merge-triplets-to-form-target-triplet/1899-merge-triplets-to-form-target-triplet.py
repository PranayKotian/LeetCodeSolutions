class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Greedy solution
        #Time: O(n) Space: O(1)
        arr = [0, 0, 0]
        
        for trip in triplets:
            valid = []
            for i,v in enumerate(trip):
                if v > target[i]:
                    valid = []
                    break
                if v == target[i]:
                    valid.append(i)
            for i in valid:
                arr[i] = 1
        
        return sum(arr) == 3