class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pac, atl = set(), set()

        def dfs(i, j, seen, prev):
            if (not 0 <= i < m or not 0 <= j < n or
                (i, j) in seen or
                heights[i][j] < prev):
                return
            seen.add((i, j))
            dfs(i + 1, j, seen, heights[i][j])
            dfs(i, j + 1, seen, heights[i][j])
            dfs(i - 1, j, seen, heights[i][j])
            dfs(i, j - 1, seen, heights[i][j])

        for i in range(m):
            dfs(i, 0, pac, 0)
            dfs(i, n - 1, atl, 0)
        for j in range(n):
            dfs(0, j, pac, 0)
            dfs(m - 1, j, atl, 0)
        
        sol = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    sol.append([i, j])


        return sol
            

            



        