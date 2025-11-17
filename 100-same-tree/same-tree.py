# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1, tree2 = [], []

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        
        def dfs(node: Optional[TreeNode], result: list):
            if not node:
                result.append(None)
                return

            result.append(node.val)
            dfs(node.left, result)
            dfs(node.right, result)
        
        dfs(p,tree1)
        dfs(q,tree2)

        print(tree1)
        print(tree2)
        return tree1 == tree2
            