# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0
    res = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def __recur(curr_node, k):
            if not curr_node or self.counter >= k:
                return

            if curr_node.left:
                self.kthSmallest(curr_node.left, k)
            self.counter += 1
            if self.counter == k:
                self.res = curr_node.val
                return
            if curr_node.right:
                self.kthSmallest(curr_node.right, k)

        __recur(root, k)

        return self.res
