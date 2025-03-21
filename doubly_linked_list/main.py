

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self, value):
        self.length = 1
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self) -> None:
        temp = self.head
        print('\n----')
        while temp is not None:
            print(f'Current Value is {temp.value}')
            # Move on to the next node until None
            temp = temp.next
        print('----\n')

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value


# ------ Pop method -------
# list = doubly_linked_list(1)
# list.append(2)
# print(list.pop())  # 2
# print(list.pop())  # 1
# print(list.pop())  # None
