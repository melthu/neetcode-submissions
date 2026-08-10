"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        otn = {}
        def dfs(node):
            otn[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in otn:
                    otn[neighbor] = dfs(neighbor)
                otn[node].neighbors.append(otn[neighbor])

            return otn[node]
                        
        return dfs(node)




        
        
        
        

        