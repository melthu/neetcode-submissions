class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        columns = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        
        for i in rows:
            matrix[i] = [0] * n
        
        for j in columns:
            for i in range(m):
                matrix[i][j] = 0
        
        
        