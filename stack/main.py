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
        print('\n---')
        while temp:
            print(temp.value)
            temp = temp.next
        print('---\n')

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node

        new_node.next, self.top = self.top, new_node
        self.height += 1
        return new_node

    def pop(self):
        if self.height == 0:
            return False

        old = self.top
        self.top = old.next
        old.next = None

        self.height -= 1
        return True


# push method
# stack = Stack(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(100)
# stack.print()
stack = Stack(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print()
print(stack.pop())
print(stack.pop())
stack.print()
