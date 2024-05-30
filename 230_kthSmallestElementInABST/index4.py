# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:

        res = 0
        counter = 0

        def dfs(node):
            nonlocal counter
            nonlocal res
            if node == None:
                return

            dfs(node.left)

            counter += 1
            if counter == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)

        return res
