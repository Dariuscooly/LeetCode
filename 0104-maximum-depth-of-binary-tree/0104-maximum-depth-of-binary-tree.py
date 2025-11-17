# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        acc = 0
        
        def dfs(node: Optional[TreeNode], count: int):
            nonlocal acc
            if not node:
                acc = max(acc, count)
                return
            
            dfs(node.right, count + 1)
            dfs(node.left, count + 1)
        
        dfs(root, acc)
        return acc

        