# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = float('inf')
        def min_height(node, height):
            nonlocal count
            if not node:
                return

            if not node.right and not node.left:
                count = min(count, height)
                return 
            
            min_height(node.left, height + 1)
            min_height(node.right, height + 1)
        
        min_height(root, 1)
        
        return count
