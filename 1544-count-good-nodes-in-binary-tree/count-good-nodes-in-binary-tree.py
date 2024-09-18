# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr_root, lst, max_value):
            if not curr_root:
                return
            if max_value <= curr_root.val:
                lst.append(curr_root.val)
                max_value = curr_root.val
            print("Head Value: "+str(max_value))
            print("Current Value: "+str(curr_root.val))
            dfs(curr_root.left, lst, max_value)
            dfs(curr_root.right, lst, max_value)
        max_value = root.val
        lst = []
        dfs(root, lst, max_value)
        return len(lst)
        