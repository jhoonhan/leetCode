# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return

        m = len(nums) // 2

        root = TreeNode(nums[m])
        # left
        root.left = self.sortedArrayToBST(nums[:m])
        # right
        root.right = self.sortedArrayToBST(nums[m + 1 :])

        return root
