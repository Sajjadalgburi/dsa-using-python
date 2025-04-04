

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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            return self.append(value)
        else:
            temp = self.head
            self.head = new_node
            temp.next.prev = new_node
            new_node.next = temp.next
            temp.next = None

            self.length += 1
            return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.prev = None
            temp.next = None

        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return False

        temp = self.head

        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    def set_node(self, index, value):
        if index < 0 or index >= self.length:
            return False

        if not self.length:
            return self.append(value)

        foundNode = self.get(index)

        foundNode.value = value

        return foundNode

    def insert(self, index, value):
        changeThisNode = self.get(index)
        if changeThisNode == False:
            return 'Cannot Do this'

        newNode = Node(value)

        newNode.next = changeThisNode
        newNode.prev = changeThisNode.prev
        changeThisNode.prev.next = newNode
        changeThisNode.prev = newNode

        self.length += 1
        return newNode

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop()

        foundNode = self.get(index)

        foundNode.prev.next = foundNode.next
        foundNode.next.prev = foundNode.prev
        foundNode.next = None
        foundNode.prev = None

        self.length -= 1
        return True


# ------ Pop method -------
# list = doubly_linked_list(1)
# list.append(2)
# print(list.pop())  # 2
# print(list.pop())  # 1
# print(list.pop())  # None
# ------ pre-append method -------
# list = doubly_linked_list(1)
# list.append(2)
# list.append(3)
# list.print_list()
# list.prepend(0)
# list.prepend(-1)
# list.print_list()
# ------ pop-first method -------
# list = doubly_linked_list(1)
# list.append(2)
# list.append(3)
# list.print_list()
# print(list.pop_first())  # True
# list.print_list()  # 2, 3
# print(list.pop_first())  # True
# print(list.pop_first())  # True
# print(list.pop_first())  # None
# list = doubly_linked_list(0)
# list.append(1)
# list.append(2)
# list.append(3)
# list.print_list()
# print(list.get(1))
# print(list.get(3))
# print(list.get(2))
# list = doubly_linked_list(0)
# list.append(1)
# list.append(2)
# list.append(3)
# list.print_list()
# list.set_node(1, 'Changed')
# list.set_node(3, 'Changed')
# list.print_list()
# list = doubly_linked_list(0)
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# list.print_list()
# list.insert(222, 'insered here')
# list.print_list()
list = doubly_linked_list(0)
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.print_list()
list.remove(3)
list.print_list()
list.remove(3)
list.print_list()
