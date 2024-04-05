# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode()
        dummy.next = head

        counter = 0

        first = None
        left_node = None

        l = dummy
        temp = head
        r = head

        while r:
            counter += 1
            r = r.next

            if counter == left:
                first = temp
                l.next = None
                left_node = l

            if left < counter <= right:
                temp.next = l

            if counter == right:
                first.next = r
                left_node.next = temp

            l = temp
            temp = r
        return dummy.next
