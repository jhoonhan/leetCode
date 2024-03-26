# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        # Find left
        dummy = ListNode()
        dummy.next = head
        left_prev = dummy
        curr = head
        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        og_left_head = curr

        # Reverse
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        og_left_head.next = curr
        left_prev.next = prev

        return dummy.next
