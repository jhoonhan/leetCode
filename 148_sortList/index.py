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

    def __merge(self, head1, head2):
        dummy = ListNode()
        head = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next

        while head1 is not None:
            head.next = head1
            head = head.next
            head1 = head1.next
        while head2 is not None:
            head.next = head2
            head2 = head2.next
            head = head.next
        return dummy.next

    def merge(self, head):
        if head == None:
            return
        if head.next == None:
            return head
        # find middle
        slow = head
        fast = head
        mid = slow
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.__merge(left, right)

    dummy = ListNode()

    def __swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val

    def __pivot(self, pivot, end):
        swap = pivot
        comp = pivot.next
        end_val = None if end == None else end.val

        while comp is not None and comp.val != end_val:
            if pivot.val > comp.val:
                swap = swap.next
                self.__swap(swap, comp)
            comp = comp.next

        self.__swap(pivot, swap)

        return swap

    def __quick_sort(self, head, right):
        right_val = right.val if right is not None else None
        head_val = head.val if head is not None else None
        if head_val != right_val:
            pvt = self.__pivot(head, right)
            self.__quick_sort(head, pvt)
            self.__quick_sort(pvt.next, right)
        return head

    def sortList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        self.dummy.next = head
        return self.__quick_sort(self.dummy.next, None)
