class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        #Dictionary Solution
        #Time: O(n) Space: O(n)
        
        table = defaultdict(int)
        for n in arr:
            table[n] += 1
        arr.sort()
        
        if table[0]%2 == 1:
            return False
        
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