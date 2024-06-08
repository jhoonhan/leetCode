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

    def selection(self, head):
        print("god is good")
        if head == None or head.next == None:
            return head

        temp = head
        while temp.next:
            min_node = temp
            curr = temp.next

            while curr:
                if curr.val < min_node.val:
                    min_node = curr
                curr = curr.next

            if curr != min_node:
                temp.val, min_node.val = min_node.val, temp.val

            temp = temp.next
        return head

    def sortList(self, head):
        print("God is good")
        if head == None or head.next == None:
            return head

        dummy = ListNode(0, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue

            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next
