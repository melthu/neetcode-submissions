class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        path = set()

        def dfs(i, j, x):
            if ((i, j) in path or
                x == len(word) or
                not (0 <= i < m) or
                not (0 <= j < n) or
                board[i][j] != word[x]
            ):
                return

            if x == len(word) - 1:
                return True

            path.add((i, j))
            for d in directions:
                di, dj = d
                if dfs(i + di, j + dj, x + 1):
                    return True
            path.remove((i, j))

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
            


            
            
            

            

            

            
        