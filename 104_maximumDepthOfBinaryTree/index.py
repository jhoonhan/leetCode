import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def __dfs(node, res):
            if node == None:
                return res
            res += 1

            left_depth = __dfs(node.left, res)
            right_depth = __dfs(node.right, res)

            return max(left_depth, right_depth)

        def __bfs(node):
            queue = collections.deque()
            if node == None:
                return 0
            res = 0
            queue.append(node)

            while queue:
                qLen = len(queue)
                for _ in range(qLen):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res += 1

            print(res)

            return res

        return __bfs(root)
