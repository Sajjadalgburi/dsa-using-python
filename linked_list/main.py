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


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append('last item')
my_linked_list.prepend(1)
my_linked_list.prepend('first item')
my_linked_list.print_list()
print(my_linked_list.pop())
print(my_linked_list.pop_first())
my_linked_list.print_list()
