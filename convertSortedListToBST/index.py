# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)

        fast = head
        slow = head
        prev_slow = slow

        while fast and fast.next:
            prev_slow = slow
            fast = fast.next.next
            slow = slow.next

        temp = slow.next

        prev_slow.next = None
        new_node = TreeNode(slow.val)
        new_node.left = self.sortedListToBST(head)
        new_node.right = self.sortedListToBST(temp)

        return new_node
