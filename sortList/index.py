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

    def selection(self, head):
        if head == None or head.next == None:
            return head

        curr = head
        while curr.next:
            min_node = curr
            inner_current = curr.next
            # Find the min_node
            while inner_current:
                if inner_current.val < min_node.val:
                    min_node = inner_current
                inner_current = inner_current.next
            # Min node found. now swap
            if curr != min_node:
                curr.val, min_node.val = min_node.val, curr.val

            curr = curr.next
        return head

    def insertion(self, head):
        if head == None or head.next == None:
            return head

        slh = head
        uslh = head.next
        slh.next = None

        while uslh is not None:
            current = uslh
            uslh = uslh.next

            # Check if current node is smaller than the first(smallest) node
            if current.val < slh.val:
                current.next = slh
                slh = current
            # If not, gotta find one that is smaller but largest among sorted list
            else:
                pointer = slh
                # Find a largest node BUT smaller than current
                while pointer.next is not None and pointer.next.val < current.val:
                    pointer = pointer.next
                # Since pointer < current < pointer.next
                # insert the current between pointer & pointer.next
                current.next = pointer.next
                pointer.next = current
        head = slh

        return head
