class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        print('\n---')
        while temp:
            print(temp.value)
            temp = temp.next
        print('---\n')

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first, self.last = new_node

        self.last.next = new_node
        self.last = new_node

        self.length += 1
        return new_node


# Enqueue method
queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print()
