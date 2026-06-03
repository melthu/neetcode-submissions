class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                r, c = q.popleft()
                for dr, dc in directions:
                    if ((r + dr in range(m)) and
                        (c + dc in range(n)) and
                        (grid[r + dr][c + dc] == "1") and
                        ((r + dr, c + dc)) not in visited):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

        visited = set()
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        return res

        


        