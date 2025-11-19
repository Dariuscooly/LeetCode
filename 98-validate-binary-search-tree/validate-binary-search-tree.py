# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node: Optional[TreeNode], low, high):
            if not node:
                return True
            

            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right,node.val, high)
        
        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = height(node.left)
            if left == -1:
                return -1
            
            right = height(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        return dfs(root, float('-inf'), float('inf'))
          