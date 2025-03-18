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

    # append item at the end of the list (1)
    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        return True


my_linked_list = LinkedList(0)
my_linked_list.get_length()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.get_length()
