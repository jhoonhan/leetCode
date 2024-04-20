# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = TreeNode(-1)
        self.counter = 0
        self.traversed = [self.root]
        self.dfs(root)

    def dfs(self, node):

        if node == None:
            return None

        self.dfs(node.left)
        self.traversed.append(node)
        self.dfs(node.right)

    def next(self) -> int:
        self.counter += 1
        if self.counter not in range(len(self.traversed)):
            return False
        self.root = self.traversed[self.counter]
        return self.root.val

    def hasNext(self) -> bool:
        if self.counter < len(self.traversed) - 1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
