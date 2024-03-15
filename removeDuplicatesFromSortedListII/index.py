class Solution(object):
    # def deleteDuplicates(self, head):
    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     # We use l (for node just before duplications begins), r (for the last node of the duplication group)...
    #     r, l = head, dummy
    #     while r:
    #         while r.next and r.val == r.next.val:
    #             r = r.next

    #         if l.next == r:
    #             l = l.next
    #             r = r.next
    #         else:
    #             l.next = r.next
    #             r = l.next

    #     return dummy.next
    def deleteDuplicates(self, head):
        # Edge case: If the linked list is empty or has only one element
        if not head or not head.next:
            return head

        # Create a dummy node to handle cases where the first few elements are duplicates
        dummy = ListNode(-1)
        dummy.next = head

        # Initialize pointers l (for the previous distinct node) and r (for the current node)
        l = dummy
        r = head

        while r and r.next:
            # If the current node's value is equal to the next node's value
            if r.val == r.next.val:
                # Move r until it points to a distinct value
                while r.next and r.val == r.next.val:
                    r = r.next
                # Skip the duplicates by assigning l's next to the distinct node
                l.next = r.next
            else:
                # Move l and r to the next distinct node
                l = l.next
            r = r.next

        return dummy.next
