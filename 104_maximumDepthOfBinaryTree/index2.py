# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        depth = 0

        def dfs(node, counter):
            if node == None:
                return

            counter += 1

            dfs(node.left, counter)
            dfs(node.right, counter)

            nonlocal depth
            depth = max(depth, counter)

        dfs(root, depth)

        return depth
