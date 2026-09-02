class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        r, c = 0, 0
        d = 0
        while len(res) < m * n:
            res.append(matrix[r][c])
            matrix[r][c] = None
            if ((not 0 <= r + directions[d][0] < m) or 
                (not 0 <= c + directions[d][1] < n) or
                (matrix[r + directions[d][0]][c + directions[d][1]] == None)):
                d = (d + 1) % 4
            r += directions[d][0]
            c += directions[d][1]

        return res

         
        