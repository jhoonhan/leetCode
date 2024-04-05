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

        l = dummy
        temp = head

        while temp:
            if temp.val in hashmap:
                hashmap[temp.val] += 1
            else:
                hashmap[temp.val] = 1
            temp = temp.next

        print(hashmap)

        return head
