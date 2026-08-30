class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = dict()
        for u, v in edges:
            if u not in G:
                G[u] = []
            if v not in G:
                G[v] = []
            G[u].append(v), G[v].append(u)

        visited = set()
        def dfs(u, parent):
            if u in visited:
                return False

            visited.add(u)
            for v in G.get(u, []):
                if v == parent:
                    continue
                dfs(v, u)
            return True

        cc = 0
        for i in range(n):
            if dfs(i, -1):
                cc += 1
        return cc
        