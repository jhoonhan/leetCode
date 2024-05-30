# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        q = deque()
        q.append(root)
        reverse = False
        while q:
            q_len = len(q)
            level = []
            for _ in range(q_len):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    level.append(cur.val)
            if reverse:
                level.reverse()
            if level:
                res.append(level)
            reverse = not reverse
        return res
