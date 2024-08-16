class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        while matrix:
            res += matrix.pop(0)
            for i in range(len(matrix)):
                if matrix[i]:
                    res.append(matrix[i].pop(-1))
            if matrix: res += matrix.pop(-1)[::-1]
            for i in range(len(matrix)-1,-1,-1):
                if matrix[i]:
                    res.append(matrix[i].pop(0))
        
        return res