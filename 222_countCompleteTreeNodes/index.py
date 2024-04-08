# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(root, acc):
            if root == None:
                return acc
            acc += 1
            left = dfs(root.left, acc)
            right = dfs(root.right, acc)

            return acc

        return dfs(root, 0)
