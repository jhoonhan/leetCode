# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(head):
            if not head:
                return None

            left = dfs(head.left)
            right = dfs(head.right)

            # Both none
            if left == None and right == None:
                return head
            # if there is left
            if left != None:
                head.left = None
                head.right = left
                temp = left
                while temp.right:
                    temp = temp.right
                temp.right = right

            return head

        dfs(root)

        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        print("aang")
