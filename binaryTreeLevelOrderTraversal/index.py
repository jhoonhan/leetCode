import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        q = collections.deque()
        q.append(root)
        level = [[root.val]]
        while q:
            q_len = len(q)
            res = []
            for _ in range(q_len):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    res.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    res.append(cur.right.val)
            if res:
                level.append(res)

        return level

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []
            for _ in range(q_len):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level)

        return res
