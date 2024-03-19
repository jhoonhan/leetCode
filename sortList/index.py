# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def bubble(self, head):
        if head == None or head.next == None:
            return

        sorted_until = None

        while sorted_until != head.next:
            current = head
            while current.next != sorted_until:
                next_node = current.next
                if current.val > next_node.val:
                    current.val, next_node.val = next_node.val, current.val
                current = current.next
            sorted_until = current

        return head

    def sortList(self, head):
        if head == None or head.next == None:
            return

        curr = head
        while curr.next:
            print(curr.val)

            min_node = curr

            temp = curr
            while temp.next:
                if temp.val < min_node.val:
                    min_node = temp
                temp = temp.next

            curr.val, min_node.val = min_node.val, curr.val

            curr = curr.next
        print(head.val)
        return head
