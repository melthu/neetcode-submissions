class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(n):
            res.append([0] * m)

        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]
        
        return res
        