# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        index = 0

        slow = index
        fast = index

        while fast < len(nums) - 1:
            slow += 1
            fast += 2

        new_node = TreeNode(nums[slow])
        left = nums[index:slow]
        right = nums[slow + 1 :]

        new_node.left = self.sortedArrayToBST(left)
        new_node.right = self.sortedArrayToBST(right)

        return new_node
