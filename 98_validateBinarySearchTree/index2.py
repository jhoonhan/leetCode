# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def __dsf(node, l, r):
            if node == None:
                return True
            if l >= node.val or node.val >= r:
                return False
            return __dsf(node.left, l, node.val) and __dsf(node.right, node.val, r)

        return __dsf(root, float("-inf"), float("inf"))
