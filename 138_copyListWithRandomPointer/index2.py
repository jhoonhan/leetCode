"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        hashmap = {None: None}

        temp = head
        while temp:
            copy = Node(temp.val)
            hashmap[temp] = copy
            temp = temp.next

        temp = head
        while temp:
            copy = hashmap[temp]
            copy.next = hashmap[temp.next]
            copy.random = hashmap[temp.random]
            temp = temp.next

        return hashmap[head]
