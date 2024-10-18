class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        #Remainders Map Solution
        #Time: O(n) Space: O(60)
        
        arr = [0] * 60
        for t in time:
            arr[t%60] += 1
        
        res = 0
        for i in range(1,30):
            res += arr[i]*arr[60-i]
        n = arr[0]
        res += n*(n-1)//2
        n = arr[30]
        res += n*(n-1)//2
        return res
        
        """
        #Groupings Solution
        #Time: O(n^2) Space: O(n)
        #TLE - 33/35
        
        table = defaultdict(list)
        for t in time:
            r = t%10
            table[r].append(t)
        
        res = 0
        for i in range(1,5):
            for t1 in table[i]:
                for t2 in table[10-i]:
                    if (t1+t2)%60 == 0:
                        res += 1
        for i in range(len(table[0])):
            for j in range(i+1,len(table[0])): 
                if (table[0][i]+table[0][j])%60 == 0:
                    res += 1
        for i in range(len(table[5])):
            for j in range(i+1,len(table[5])): 
                if (table[5][i]+table[5][j])%60 == 0:
                    res += 1
        return res
        
        
        #Brute Force Solution
        #Time: O(n^2) Space: O(1)
        #TLE - 30/35
        
        res = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i]+time[j])%60 == 0:
                    res += 1
        return res
        """