import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            res = []
            for _ in range(q_len):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    res.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    res.append(cur.right)
            if res:
                for i in range(len(res)):
                    if i + 1 < len(res):
                        res[i].next = res[i + 1]
                    else:
                        res[i].next = None

        return root
