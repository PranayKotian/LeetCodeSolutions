class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Efficient solution?
        #Time: O(n) Space: O(n)
        
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = count.get(n,0) + 1
        
        while count:
            minVal = min(count.keys())
            for i in range(groupSize):
                if minVal not in count:
                    return False
                count[minVal] -= 1
                if count[minVal] == 0:
                    del count[minVal]
                minVal += 1
        
        return True
        
        """
        #Inefficient solution
        #Time: O(n^2) Space: O(n)
        if len(hand) % groupSize != 0:
            return False
        
        #O(nlogn) operation
        hand.sort()
        
        while hand:
            minVal = hand.pop(0)
            for i in range(groupSize-1):
                minVal += 1
                if minVal not in hand:
                    return False
                hand.remove(minVal) #O(n) operation
        return True
        """