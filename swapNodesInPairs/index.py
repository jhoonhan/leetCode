# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            after = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = after
            prev.next = second

            prev = curr
            curr = after

        return dummy.next
