class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        
        while hand:
            minVal = hand.pop(0)
            for i in range(groupSize-1):
                minVal += 1
                if minVal not in hand:
                    return False
                hand.remove(minVal)
        return True