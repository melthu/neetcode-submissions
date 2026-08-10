class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        sol = 0

        def bfs(r, c):
            q = deque()
            q.append((i, j))
            grid[i][j] = '0'
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n:
                        if grid[r + dr][c + dc] == '1':
                            q.append([r + dr, c + dc])
                            grid[r + dr][c + dc] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    sol += 1

        return sol
                

                        
                        





        