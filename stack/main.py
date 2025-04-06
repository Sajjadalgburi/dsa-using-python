class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node

        new_node.next, self.top = self.top, new_node
        self.height += 1
        return new_node


# push method
# stack = Stack(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(100)
# stack.print()
