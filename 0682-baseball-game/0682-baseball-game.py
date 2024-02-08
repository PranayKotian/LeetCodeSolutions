class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        #Solution 1: Stack
        #Time: O(n) Space: O(n)
        #(solution assumes no invalid operations)
        
        record = []
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1]*2)
            elif op == "+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(op))
        
        return sum(record)