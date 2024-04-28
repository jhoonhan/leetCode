# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        l = dummy
        r = head
        delay = n
        while r:
            if delay <= 0:
                l = l.next

            r = r.next
            delay -= 1

        temp = l.next.next
        l.next = temp

        return dummy.next
