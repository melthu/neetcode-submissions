class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def bfs(i, j):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            area = 1

            q = collections.deque()
            q.append((i, j))
            seen.add((i, j))
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    if ((i + di in range(m)) and
                        (j + dj in range(n)) and
                        (grid[i + di][j + dj] == 1) and
                        ((i + di, j + dj) not in seen)):
                        q.append((i + di, j + dj))
                        seen.add((i + di, j + dj)) 
                        area += 1
            return area

        seen = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in seen:
                    res = max(res, bfs(r, c))
                    print(res)
                    print()
                    
        return res
        