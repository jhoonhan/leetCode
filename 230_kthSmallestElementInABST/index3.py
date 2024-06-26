# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None

        counter = 0
        res = 0

        def dfs(node):
            nonlocal res
            nonlocal counter

            if node == None:
                return

            dfs(node.left)
            counter += 1
            if counter == k:
                res = node.val
            dfs(node.right)

        dfs(root)

        return res
