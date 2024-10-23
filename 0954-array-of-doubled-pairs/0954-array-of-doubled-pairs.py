class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        #Dictionary Solution Optimized
        #Time: O(nlogn) Space: O(n)
        
        table = Counter(arr)
        for n in sorted(arr, key=abs):
            if table[n] == 0:
                continue
            if table[n*2] == 0:
                return False
            table[n] -= 1
            table[n*2] -= 1
        return True
    
        """
        #Dictionary Solution
        #Time: O(nlogn) Space: O(n)
        
        table = Counter(arr)
        arr.sort()
        
        for n in arr:
            if table[n] == 0:
                continue
            if n < 0:
                if n%2 != 0 or table[n//2] == 0:
                    return False
                table[n] -= 1
                table[n//2] -= 1
            else:
                if table[n*2] == 0:
                    return False
                table[n] -= 1
                table[n*2] -= 1
        return True
        """