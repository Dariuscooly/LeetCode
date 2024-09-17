# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(curr_root, leaves):
            if not curr_root:
                return
            if not curr_root.left and not curr_root.right:
                leaves.append(curr_root.val)
            dfs(curr_root.left, leaves)
            dfs(curr_root.right, leaves)
        

        root1_leaves = []
        root2_leaves = []
        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)

        return root1_leaves == root2_leaves


    
