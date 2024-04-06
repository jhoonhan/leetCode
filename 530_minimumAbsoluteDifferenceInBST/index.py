# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def __dfs(curr_node):
            if not curr_node:
                return
            if curr_node.left:
                __dfs(curr_node.left)
            nodes.append(curr_node.val)
            if curr_node.right:
                __dfs(curr_node.right)

        __dfs(root)

        min_diff = float("inf")
        for i in range(1, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i - 1])

        return min_diff
