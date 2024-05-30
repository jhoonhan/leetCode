# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0, head)

        counter = 0

        node_before_reverse = None
        new_tail = None

        before = dummy
        temp = head
        after = head

        while after:
            counter += 1
            after = after.next

            if counter == left:
                node_before_reverse = before
                before.next = None
                new_tail = temp

            if left < counter <= right:
                temp.next = before

            if counter == right:
                new_tail.next = after
                node_before_reverse.next = temp

            before = temp
            temp = after

        return dummy.next
