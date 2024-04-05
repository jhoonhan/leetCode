# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}

        temp = head
        while temp:
            if temp.val in hashmap:
                hashmap[temp.val].next = temp.next
            else:
                hashmap[temp.val] = temp

            temp = temp.next
        return head
