class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        #Sorting solution
        #Time: O(nlogn) Space: O(1)
        
        prices.sort()
        if prices[0] + prices[1] > money:
            return money
        else:
            return money - prices[0] - prices[1]
        
        """
        #One pass solution
        #Time: O(n) Space: O(1)
        
        mins = [sys.maxsize, sys.maxsize]
        for p in prices:
            if p < mins[0]:
                mins[0], mins[1] = p, mins[0]
            elif p < mins[1]:
                mins[1] = p

        if sum(mins) > money:
            return money
        else:
            return money - sum(mins)
        """