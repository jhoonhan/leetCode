# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        hashmap = {}
        temp = head
        prev = dummy

        while temp:
            if temp.val in hashmap:
                hashmap[temp.val] += 1
            else:
                hashmap[temp.val] = 1
            temp = temp.next

        temp = head
        prev = dummy
        while temp:
            if hashmap[temp.val] > 1:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return dummy.next
