# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # preorder
        res = 0

        def dfs(node, acc):
            nonlocal res
            if node == None:
                return

            temp = acc + str(node.val)

            if node.left or node.right:
                dfs(node.left, temp)
                dfs(node.right, temp)
            else:
                res += int(temp)

        dfs(root, "")

        return res
