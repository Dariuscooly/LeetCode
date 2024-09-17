# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr_root, depth):
            if not curr_root:
                return depth
            return max(dfs(curr_root.left, depth + 1), dfs(curr_root.right, depth + 1))
        return dfs(root,0)

        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1