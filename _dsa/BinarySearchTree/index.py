class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # def insert2(self, value, root=False):
    #     print(f"Recursive")
    #     new_node = Node(value)
    #     temp = root
    #     if root is False:
    #         temp = self.root

    #     if temp == None:
    #         self.root = new_node
    #         print(f"Added: {new_node.value}")

    #         return True
    #     else:
    #         if new_node.value == temp.value:
    #             return False
    #         if new_node.value < temp.value:
    #             return self.insert2(value, temp.left)
    #         if new_node.value > temp.value:
    #             return self.insert2(value, temp.right)


bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contains(3))
