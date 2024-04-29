# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        print("God is good")
        prev = None
        res = float("inf")

        def dfs(node):
            nonlocal prev, res

            if not node:
                return

            dfs(node.left)
            if prev != None:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)

        return res
