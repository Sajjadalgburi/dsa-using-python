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


tree = BinarySearchTree()
tree.insert(2)
tree.insert(3)
tree.insert(1)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
