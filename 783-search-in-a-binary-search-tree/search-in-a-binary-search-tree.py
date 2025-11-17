# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return []
        index = {}
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            
            index[node.val] = node
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return index.get(val)

