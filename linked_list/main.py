'''
---Big O for Linked List

method - append()
Appending to the last element is Big O(1) constant time because
nothing is moved, rather the tail is changed to point at the new node
-----
method - pop()
Popping the last element is Big O(n) linear time because
we start at head since we have no refrence to the old tail, iterate through every node,
after that we can find the new last node and point that to tail
-----
method - add()
Adding to the first element is Big O(1) constant time because
nothing is moved, rather the head is changed to point at the new node
-----

Additional Stuff
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def get_length(self):
        print(f"\n length of the Linked List is: {self.length}")

    def print_list(self):
        temp = self.head
        print('\n----')
        while temp is not None:
            print(f'Current Value is {temp.value}')
            # Move on to the next node until None
            temp = temp.next
        print('----\n')

    # append item at the end of the list (1)
    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    # method to pop an item from the LL. This is Big O(n) where n is the lenght of the list
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # method to add to the begining of the linked lost. Big O(1) constant time
    def prepend(self, value):
        if self.length is None:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    # method to remove node from the begining of the linked lost. Big O(1) constant time
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    # get method to return the value of a given index. Big O (n) where n is the size of the LL worst case
    def get(self, index):
        if index < 0 or index >= self.length:
            return 'Out of boundry'

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    # set method to change the value of a give node in an index. Big O (n) where n is the size of the LL worst case
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        temp = self.head
        prev = self.head

        new_node = Node(value)
        for _ in range(index):
            prev = temp
            temp = temp.next

        prev.next = new_node
        new_node.next = temp

        self.length += 1
        return True

    def remove(self, index):
        if self.length is None:
            return None

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop()

        temp = self.head
        pre = self.head
        for _ in range(index):
            pre = temp
            temp = temp.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        if self.length is None:
            return False

        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        while after:
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# -- Random --
# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.append('last item')
# my_linked_list.prepend(1)
# my_linked_list.prepend('first item')
# my_linked_list.print_list()
# print(my_linked_list.pop())
# print(my_linked_list.pop_first())
# my_linked_list.print_list()
# ---------------------------------------
# -- For Set value --
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.print_list()
# print(my_linked_list.get(3))
# print(my_linked_list.get(100))
# print(my_linked_list.set_value(2, 'set value'))
# my_linked_list.print_list()
# ---------------------------------------
# -- For Inserting --
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_list()
# print(my_linked_list.insert(1, '1 - inserted'))
# my_linked_list.print_list()
# -- For Remove Method --
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.print_list()
# print(my_linked_list.remove(3))
# my_linked_list.print_list()
# print(my_linked_list.remove(3))
# my_linked_list.print_list()
# -- For Remove Method --
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
