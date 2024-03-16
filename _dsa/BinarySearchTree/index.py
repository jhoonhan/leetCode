class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.