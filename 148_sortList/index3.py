# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def bubble(self, head):
        if head == None or head.next == None:
            return head
        sorted_until = None

        while sorted_until != head.next:
            current = head
            while sorted_until != current.next:
                next_node = current.next
                if current.val > next_node.val:
                    current.val, next_node.val = next_node.val, current.val
                current = current.next
            sorted_until = current

        return head
