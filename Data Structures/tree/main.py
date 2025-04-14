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
        if not self.root:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                # add to the left
                if not temp.left:  # or if temp.left is None
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                # we know it is greater than the root
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if not self.root:
            return False

        if self.root.value == value:
            return True

        temp = self.root

        while True:
            if temp.value == value:
                return True

            if temp.value > value:
                if not temp.left:
                    return False
                temp = temp.left
            else:
                if not temp.right:
                    return False
                temp = temp.right


# Tree insert method
# tree = BinarySearchTree()
# tree.insert(2)
# tree.insert(3)
# tree.insert(9)
# tree.insert(5)
# tree.insert(7)
# tree.insert(6)
# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.right.value)

# Tree Contains method
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
print(tree.contains(27))  # returns True
print(tree.contains(17))  # returns False
