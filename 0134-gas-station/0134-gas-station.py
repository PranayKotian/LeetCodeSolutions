class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Greedy solution
        #Time: O(n) Space: O(1)
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        total = 0 
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                res = i+1
                total = 0
        return res
        
        '''
        #Quadratic solution
        #Time: O(n^2) Space: O(1)
        if sum(cost) > sum(gas):
            return -1
        
        n = len(gas)
        gas = gas+gas
        cost = cost+cost
        
        for i in range(n):
            if gas[i] < cost[i] or gas[i]==0:
                continue
            curGas = 0
            for j in range(i,i+n):
                curGas += gas[j] - cost[j]
                if curGas < 0:
                    break
                if j == i+n-1:
                    return i
        '''