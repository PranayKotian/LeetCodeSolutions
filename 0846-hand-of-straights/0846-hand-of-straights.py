class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        #Inefficient Solution
        #Time: O(n^2) Space: O(1)
        
        if len(hand) % groupSize != 0:
            return False
        
        #Smallest values will always need consecutive numbers
        hand.sort()
        while hand:
            i = hand[0]
            for j in range(1, groupSize):
                if i+j not in hand:
                    return False
            hand.remove(i)
            for j in range(1, groupSize):
                hand.remove(i+j)
        return True 