class Stack:
    def __init__(self):
        self.stack_list = []
        self.length = len(self.stack_list)

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)
        self.length += 1

    def pop(self):
        if not len(self.stack_list):
            return None
        popped_node = self.stack_list.pop()
        return popped_node


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1
 
"""
