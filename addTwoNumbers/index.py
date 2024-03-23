# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode()
        res_head = dummy

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = carry + val1 + val2
            carry = val // 10
            res_head.next = ListNode(val % 10)
            res_head = res_head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            res_head.next = ListNode(carry)

        return dummy.next


print(0 // 10)
