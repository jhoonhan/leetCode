# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __r_insert(self, currentNode, value):
        if currentNode == None:
            return TreeNode(value)
        if currentNode.value > value:
            currentNode.left = self.__r_insert(currentNode.left, value)
        if currentNode.value < value:
            currentNode.right = self.__r_insert(currentNode.right, value)
        return currentNode

    def r_insert(self, currentNode, value):
        self.__r_insert(currentNode, value)

    def sortedListToBST(self, head):
        if head == None:
            return []
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next


sol = Solution()
sol.sortedListToBST([-10, -3, 0, 5, 9])
