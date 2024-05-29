# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode()
        temp = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_val = val1 + val2 + carry
            remain_val = sum_val % 10
            carry = sum_val // 10

            temp.next = ListNode(remain_val)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            temp.next = ListNode(carry)

        return dummy.next
