# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        def __dfs(current_node, l, r):
            if not current_node:
                return True

            if not (current_node.val < r and current_node.val > l):
                return False

            return __dfs(current_node.left, l, current_node.val) and __dfs(
                current_node.right, current_node.val, r
            )

        return __dfs(root, float("-inf"), float("inf"))
