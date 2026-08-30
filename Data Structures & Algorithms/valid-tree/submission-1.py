class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        G = dict()
        for u, v in edges:
            if u not in G:
                G[u] = []
            if v not in G:
                G[v] = []
            G[u].append(v), G[v].append(u)
        
        state = [0] * n

        def dfs(u, parent):
            if state[u] == 2:
                return True
            if state[u] == 1:
                return False

            state[u] = 1
            
            for v in G.get(u, []):
                if v == parent:
                    continue
                if not dfs(v, u):
                    return False
            
            state[u] = 2
            return True

        for i in range(n):
            if not dfs(i, -1):
                return False
            
        return True
        