# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = []

        # if root == None:
        #     return None

        # def __traverse(curr_node):
        #     if curr_node.left is not None:
        #         __traverse(curr_node.left)
        #     # In order
        #     res.append(curr_node.val)
        #     if curr_node.right is not None:
        #         __traverse(curr_node.right)

        # __traverse(root)

        # return res[k - 1]

        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            cur = cur.right
