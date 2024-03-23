"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head):
        hash = {None: None}
        temp = head
        while temp:
            copy = Node(temp.val)
            hash[temp] = copy
            temp = temp.next

        temp = head
        while temp:
            copy = hash[temp]
            copy.next = hash[temp.next]
            copy.random = hash[temp.random]
            temp = temp.next

        return hash[head]
