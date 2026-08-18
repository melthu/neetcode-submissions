# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, level):
            if not node:
                return

            if len(sol) < level:
                sol.append([])
            sol[level - 1].append(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        sol = []
        traverse(root, 1)
        return sol


        


        