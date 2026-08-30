class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = dict()
        for v, u in prerequisites:
            if u not in G:
                G[u] = []
            G[u].append(v)

        n = numCourses
        state = [0] * n
        def dfs(u):
            if state[u] == 2:
                return True
            if state[u] == 1:
                return False

            state[u] = 1
            for v in G.get(u, []):
                if not dfs(v):
                    return False

            state[u] = 2
            return True
        
        sol = True
        for i in range(n):
            if not dfs(i):
                sol = False

        return sol


        



        