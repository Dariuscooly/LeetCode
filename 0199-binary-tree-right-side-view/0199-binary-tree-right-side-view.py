# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(curr_root, lst_right, depth):
            if not curr_root:
                return
            if depth == len(lst_right):
                lst_right.append(curr_root.val)
            dfs(curr_root.right, lst_right, depth + 1)
            dfs(curr_root.left, lst_right, depth + 1)
        lst_right = []
        dfs(root, lst_right, 0)
        return lst_right